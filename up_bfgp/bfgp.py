import os
import shutil
import subprocess
from typing import Optional, Callable, List, Union, IO
from unified_planning.engines.results import PlanGenerationResultStatus
import unified_planning as up
from unified_planning.model import ProblemKind
from unified_planning.engines import LogMessage
import sys
from unified_planning.io import PDDLReader
from unified_planning.plans.sequential_plan import SequentialPlan
import pkg_resources
import unified_planning.engines as engines
from unified_planning.io.pddl_writer import PDDLWriter
import tempfile
from unified_planning.engines.pddl_planner import PDDLPlanner


class BestFirstGeneralizedPlanner(engines.Engine, engines.mixins.FewshotPlannerMixin):
    """ BFGP++ is a Generalized PDDLPlanner, which in turn is an Engine & FewshotPlanner """

    def __init__(self, **options):
        # Read known user-options and store them for using in the `solve` method
        engines.Engine.__init__(self)
        engines.mixins.FewshotPlannerMixin.__init__(self)
        self.credits = {
            "name": "BFGP++",
            "author": "Javier Segovia-Aguas, Sergio Jiménez, Anders Jonsson and collaborators",
            "contact": "javier.segovia@upf.edu (for UP integration)",
            "website": "bfgp_pp website",
            "license": "GPLv3",
            "short_description": "A framework based on BFGP where solutions are either assembly-like programs, or "
                                 "structured programs that are syntactically terminating.",
            "long_description": "A framework based on Best-First Generalized Planning where solutions are either "
                                "assembly-like programs, or structured programs that are syntactically terminating.",
        }
        self.set_arguments(**options)

    def set_arguments(self, **options):
        self._mode = options.get('mode', 'synthesis')
        self._theory = options.get('theory', 'cpp')
        self._program_lines = options.get('program_lines', 10)
        self._problem_folder = options.get('problem_folder', '..')
        self._evaluation_functions = options.get('evaluation_functions', None)

    @property
    def name(self) -> str:
        return self.credits['name']

    @staticmethod
    def supported_kind():
        """See unified_planning.model.problem_kind.py for more options """
        supported_kind = ProblemKind()
        supported_kind.set_problem_class("ACTION_BASED")
        supported_kind.set_typing("FLAT_TYPING")
        supported_kind.set_typing("HIERARCHICAL_TYPING")
        supported_kind.set_conditions_kind("NEGATIVE_CONDITIONS")
        supported_kind.set_conditions_kind("EQUALITIES")
        supported_kind.set_quality_metrics("PLAN_LENGTH")
        return supported_kind

    @staticmethod
    def supports(problem_kind) -> bool:
        return problem_kind <= BestFirstGeneralizedPlanner.supported_kind()

    @staticmethod
    def preprocess(domain_filename: str, problem_filenames: List[str]) -> str:
        dest_dir = "tmp/"
        shutil.rmtree(dest_dir, ignore_errors=True)
        os.makedirs(dest_dir)
        translator = pkg_resources.resource_filename(__name__, "bfgp_pp/preprocess/pddl_translator.py")
        assert problem_filenames
        for idx, problem_filename in enumerate(problem_filenames):
            cmd = f"python {translator} -d {domain_filename} -i {problem_filename} -o {dest_dir} -id {idx + 1}"
            subprocess.run(cmd.split())
        return dest_dir

    def get_cmd(self, domain_filename: str, problem_filenames: List[str], plan_filename: str) -> List[str]:
        compiled_folder = self.preprocess(domain_filename=domain_filename, problem_filenames=problem_filenames)
        # print(compiled_folder)
        main_bin = pkg_resources.resource_filename(__name__, "bfgp_pp/main.bin")
        command = f"{main_bin} -m {self._mode} -t {self._theory} -l {self._program_lines} " \
                  f"-f {compiled_folder} -o {plan_filename}".split()
        # print(command)
        return command

    def _solve(self,
               problems: List["up.model.AbstractProblem"],
               heuristic: Optional[Callable[["up.model.state.State"], Optional[float]]] = None,
               timeout: Optional[float] = None,
               output_stream: Optional[IO[str]] = None) -> List["up.engines.results.PlanGenerationResult"]:
        # Step 1. preprocess all problems and get command (some code reused from PDDL planner)
        assert problems
        for problem in problems:
            assert isinstance(problem, up.model.Problem)
        # logs: List["up.engines.results.LogMessage"] = []
        with tempfile.TemporaryDirectory() as tempdir:
            domain_filename = os.path.join(tempdir, "domain.pddl")
            problem_filenames = [f"{tempdir}/{idx}.pddl" for idx in range(1, 1 + len(problems))]
            plan_filename = os.path.join(tempdir, "generalized_plan.prog")
            self.pddl_writers = []
            for idx, problem_filename in enumerate(problem_filenames):
                self.pddl_writers.append(PDDLWriter(problems[idx]))
                self.pddl_writers[-1].write_domain(domain_filename)
                self.pddl_writers[-1].write_problem(problem_filename)
            cmd = self.get_cmd(domain_filename, problem_filenames, plan_filename)

            # Step 2. run command (search a GP plan)
            subprocess.run(cmd)

            # Step 3. generate plans
            main_bin = pkg_resources.resource_filename(__name__, "bfgp_pp/main.bin")
            cmd = f"{main_bin} -m validation-prog -t {self._theory} -f tmp/ -p {plan_filename}".split()
            subprocess.run(cmd)
            subprocess.run('mv plan.* tmp/', shell=True)

        # Step 4. validate plans and return a list of results
        results = []
        for idx, problem in enumerate(problems):
                # Building candidate plan (from root folder)
                plan_file = f"tmp/plan.{idx+1}"
                plan = up.plans.SequentialPlan([])
                with open(plan_file) as pf:
                    for line in pf:
                        if line[0] == ';':
                            continue
                        # Extract action and params data
                        grounded_act = line[1:-2].split()
                        a = self.pddl_writers[idx].get_item_named(grounded_act[0])
                        params = []
                        for param in grounded_act[1:]:
                            params.append(self.pddl_writers[idx].get_item_named(param))
                        # Build an ActionInstance with previous data
                        plan.actions.append(up.plans.ActionInstance(action=a, params=params))
                if problem.environment.factory.PlanValidator(name='sequential_plan_validator').validate(problem, plan):
                    results.append(PlanGenerationResultStatus.SOLVED_SATISFICING)
                else:
                    results.append(PlanGenerationResultStatus.UNSOLVABLE_PROVEN)
        return results

# Register the solver
# env = up.environment.get_environment()
# env.factory.add_engine('bfgp', __name__, 'BestFirstGeneralizedPlanner')


def run_bfgp():
    # Invoke planner
    with up.environment.get_environment().factory.FewshotPlanner(name='bfgp') as bfgp:
        bfgp.set_arguments(program_lines=15)
        reader = PDDLReader()
        pddl_problem = reader.parse_problem('bfgp_pp/domains/gripper/domain.pddl', 'bfgp_pp/domains/gripper/p01.pddl')
        # print(pddl_problem)
        result = bfgp.solve([pddl_problem], output_stream=sys.stdout)
        if all(r == PlanGenerationResultStatus.SOLVED_SATISFICING for r in result):
            print(f'{bfgp.name} found a valid generalized plan!')
            # print(f'The plan is:')
            # print('\n'.join(str(x) for x in result.plan.actions))
        else:
            print('No generalized plan found!')


if __name__ == "__main__":
    run_bfgp()
