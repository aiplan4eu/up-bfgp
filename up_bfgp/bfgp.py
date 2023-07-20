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
import argparse


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
            "website": "https://github.com/jsego/bfgp-pp",
            "license": "GPLv3",
            "short_description": "Best-First Generalized Planner",
            "long_description": "A framework based on Best-First Generalized Planning that synthesizes and validates "
                                "assembly-like and structured programs.",
        }
        self.set_arguments(**options)

    def set_arguments(self, **options):
        """ Mandatory args """
        self._mode : str = options.get('mode', 'synthesis')
        self._theory : str = options.get('theory', 'cpp')
        self._program_lines : int = options.get('program_lines', 10)  # only in synthesis
        self._program : str = options.get('program', None)  # only in validation (optional for synthesis as output)

        """ Optional args """
        self._evaluation_functions : List[str] = options.get('evaluation_functions', None)  # only in synthesis
        self._num_extra_pointers : int = options.get('num_extra_pointers', 0)
        self._output_dir : str = options.get('output_dir', 'tmp/')

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

    def preprocess(self, domain_filename: str, problem_filenames: List[str]) -> None:
        #shutil.rmtree(self._output_dir, ignore_errors=True)
        os.makedirs(self._output_dir, exist_ok=True)
        subprocess.run(f"rm -rf {self._output_dir}/*.txt", shell=True)  # delete all .txt files (domain and instances)
        translator = pkg_resources.resource_filename(__name__, "bfgp_pp/preprocess/pddl_translator.py")
        assert problem_filenames
        for idx, problem_filename in enumerate(problem_filenames):
            cmd = f"python {translator} -d {domain_filename} -i {problem_filename} -o {self._output_dir} -id {idx + 1}"
            subprocess.run(cmd.split())

    def get_base_cmd(self,  domain_filename: str, problem_filenames: List[str]) -> str:
        self.preprocess(domain_filename=domain_filename, problem_filenames=problem_filenames)
        # print(compiled_folder)
        main_bin = pkg_resources.resource_filename(__name__, "bfgp_pp/main.bin")
        return f"{main_bin} -m {self._mode} -t {self._theory} -f {self._output_dir} -s {self._num_extra_pointers}"

    def get_synth_cmd(self, domain_filename: str, problem_filenames: List[str]) -> List[str]:
        """ Command to execute the generalized planner to synthesize a program """
        command = self.get_base_cmd(domain_filename, problem_filenames)
        if not (self._evaluation_functions is None):
            command += f" -e " + " ".join(self._evaluation_functions)
        command += f" -l {self._program_lines} -o {self._output_dir}/{self._program}"
        print(command)
        return command.split()

    def get_val_cmd(self, domain_filename: str, problem_filenames: List[str]) -> List[str]:
        """ Command to execute the validation of a program over a set of instances """
        command = self.get_base_cmd(domain_filename, problem_filenames)
        command += f" -p {self._output_dir}/{self._program}"
        # print(command)
        return command.split()

    def _solve(self,
               problems: List["up.model.AbstractProblem"],
               heuristic: Optional[Callable[["up.model.state.State"], Optional[float]]] = None,
               timeout: Optional[float] = None,
               output_stream: Optional[IO[str]] = None) -> List["up.engines.results.PlanGenerationResult"]:

        # Step 0. Assert that problems exist, and they are instances of up.model.Problem
        assert problems
        assert all((isinstance(p, up.model.Problem) for p in problems))

        # Step 1. preprocess all problems and get command (some code reused from PDDL planner)
        # logs: List["up.engines.results.LogMessage"] = []
        with tempfile.TemporaryDirectory() as tempdir:
            domain_filename = os.path.join(tempdir, "domain.pddl")
            problem_filenames = [f"{tempdir}/{idx}.pddl" for idx in range(1, 1 + len(problems))]
            if self._program is None:
                self._program = "dk.prog"  # os.path.join(tempdir, "dk.prog")
            self.pddl_writers = []
            for idx, problem_filename in enumerate(problem_filenames):
                self.pddl_writers.append(PDDLWriter(problems[idx]))
                self.pddl_writers[-1].write_domain(domain_filename)
                self.pddl_writers[-1].write_problem(problem_filename)

            # Step 2. search a GP plan if called in synthesis mode
            if self._mode == "synthesis":
                cmd = self.get_synth_cmd(domain_filename, problem_filenames)
                subprocess.run(cmd)  # ToDo: capture execution errors in results? e.g. INTERNAL_ERROR
            # ToDo: implement here the call to 3rd Deliverable mode

            # Step 3. generate plans
            if self._mode == "synthesis":
                self._mode = "validation-prog"  # change to validation-prog to validate the generalized plan
            else:
                assert not (self._program is None)
                assert self._mode in ["validation-prog", "validation-cpp"]  # assert is a correct validation mode

            cmd = self.get_val_cmd(domain_filename, problem_filenames)
            subprocess.run(cmd)  # ToDo: capture execution errors in results? e.g. INTERNAL_ERROR
            subprocess.run(f'mv plan.* {self._output_dir}', shell=True)

        # Step 4. validate plans and return a list of results
        return self.get_results(problems)

    def get_results(self,problems: List["up.model.AbstractProblem"]) -> List["up.engines.results.PlanGenerationResult"]:
        results = []
        for idx, problem in enumerate(problems):
            # Building candidate plan (from root folder)
            plan_file = f"{self._output_dir}/plan.{idx+1}"
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
    # Get arguments
    mode_choices = ["synthesis", "validation-prog", "validation-cpp"]
    theory_choices = ["assembler", "cpp"]

    parser = argparse.ArgumentParser(description="BFGP++ Runner",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-d", "--input_domain", type=str, required=True)
    parser.add_argument("-i", "--input_problems", type=str, nargs="+", required=True)
    parser.add_argument("-m", "--mode", choices=mode_choices, default="synthesis", required=False)
    parser.add_argument("-t", "--theory", choices=theory_choices, default="cpp", required=False)

    parser.add_argument("-l", "--program_lines", type=int, default=10, required=False)
    parser.add_argument("-p", "--program", type=str, required=False)
    parser.add_argument("-f", "--evaluation_functions", nargs="*", default=None, required=False)
    parser.add_argument("-s", "--num_extra_pointers", type=int, required=False, default=0)
    parser.add_argument("-o", "--output_dir", type=str, required=False, default="tmp/")

    args = parser.parse_args()
    args_dict = vars(args)
    domain = args.input_domain
    problems = args.input_problems

    # Invoke planner
    with up.environment.get_environment().factory.FewshotPlanner(name='bfgp') as bfgp:
        # OLD
        # bfgp.set_arguments(program_lines=15)
        # reader = PDDLReader()
        # pddl_problem = reader.parse_problem('bfgp_pp/domains/gripper/domain.pddl', 'bfgp_pp/domains/gripper/p01.pddl')
        # print(pddl_problem)
        # result = bfgp.solve([pddl_problem], output_stream=sys.stdout)
        # END OLD

        # NEW
        bfgp.set_arguments(**args_dict)
        reader = PDDLReader()
        pddl_problems = [reader.parse_problem(domain, p) for p in problems]
        result = bfgp.solve(pddl_problems, output_stream=sys.stdout)
        # END NEW

        if all(r == PlanGenerationResultStatus.SOLVED_SATISFICING for r in result):
            print(f'{bfgp.name} found a valid generalized plan!')
            # print(f'The plan is:')
            # print('\n'.join(str(x) for x in result.plan.actions))
        else:
            print('No generalized plan found!')


if __name__ == "__main__":
    run_bfgp()
