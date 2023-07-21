from unified_planning.shortcuts import *  # type: ignore
from unified_planning.io import PDDLReader
from collections import namedtuple  # type: ignore
from unified_planning.plans import PlanKind  # type: ignore
import unittest
from unified_planning.engines.results import PlanGenerationResultStatus
import up_bfgp


class BFGPtest(unittest.TestCase):
    def base_bfgp_test(self, domain_file: str, problem_files: List[str], args: dict):
        with up.environment.get_environment().factory.FewshotPlanner(name='bfgp') as bfgp:
            bfgp.set_arguments(**args)
            pddl_problems = [PDDLReader().parse_problem(domain_file, prob_file) for prob_file in problem_files]
            # Compute the generalized plan for these PDDL problems
            result = bfgp.solve(pddl_problems, output_stream=sys.stdout)
            # Check whether all generated plans are satisficing
            assert all(r == PlanGenerationResultStatus.SOLVED_SATISFICING for r in result)

    def test_bfgp_synthesis_gripper(self):
        """Testing the BFGP++ solvers can solve 3 different Gripper instances"""
        domain = 'domains/gripper/domain.pddl'
        problems = [f'domains/gripper/p{i:02}.pddl' for i in range(1, 4)]
        kwargs = dict({'mode': 'synthesis',
                       'theory': 'cpp',
                       'program_lines': 10,
                       'program': 'gripper.prog',
                       'output_dir': 'test_gripper/'})

        self.base_bfgp_test(domain_file=domain, problem_files=problems, args=kwargs)

    #@unittest.skip
    def test_bfgp_visitall(self):
        """Testing the BFGP++ solver can solve 10 different Visitall instances"""
        domain = 'domains/visitall/synthesis/domain.pddl'
        problems = [f'domains/visitall/synthesis/p{i:02}.pddl' for i in range(1, 11)]
        kwargs = dict({'mode': 'synthesis',
                       'theory': 'cpp',
                       'program_lines': 16,
                       'program': 'visitall.prog',
                       'output_dir': 'test_visitall/'})

        self.base_bfgp_test(domain_file=domain, problem_files=problems, args=kwargs)

        """Testing the BFGP++ solver can validate 10 different and larger Visitall instances"""
        domain = 'domains/visitall/validation/domain.pddl'
        problems = [f'domains/visitall/validation/p{i:02}.pddl' for i in range(1, 11)]
        kwargs = dict({'mode': 'validation-prog',
                       'theory': 'cpp',
                       'program': 'visitall.prog',
                       'output_dir': 'test_visitall/'})

        self.base_bfgp_test(domain_file=domain, problem_files=problems, args=kwargs)


if __name__ == "__main__":
    unittest.main()
