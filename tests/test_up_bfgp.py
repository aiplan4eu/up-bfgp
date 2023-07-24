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

    # @unittest.skip
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

    # @unittest.skip
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

    # @unittest.skip
    def test_bfgp_spanner(self):
        """Testing the BFGP++ solver can solve 10 first Spanner instances"""
        domain = 'domains/spanner/domain.pddl'
        problems = [f'domains/spanner/training/easy/p{i:02}.pddl' for i in range(1, 11)]
        kwargs = dict({'mode': 'synthesis',
                       'theory': 'cpp',
                       'program_lines': 16,
                       'program': 'spanner.prog',
                       'output_dir': 'test_spanner/'})

        self.base_bfgp_test(domain_file=domain, problem_files=problems, args=kwargs)

        """Testing the BFGP++ solver can validate 10 last (and larger) Spanner instances"""
        domain = 'domains/spanner/domain.pddl'
        problems = [f'domains/spanner/training/easy/p{i:02}.pddl' for i in range(90, 100)]
        kwargs = dict({'mode': 'validation-prog',
                       'theory': 'cpp',
                       'program': 'spanner.prog',
                       'output_dir': 'test_spanner/'})

        self.base_bfgp_test(domain_file=domain, problem_files=problems, args=kwargs)

    # @unittest.skip
    def test_bfgp_miconic(self):
        """Testing the BFGP++ solver can solve 50 first Miconic instances"""
        domain = 'domains/miconic/domain.pddl'
        problems = [f'domains/miconic/training/easy/p{i:02}.pddl' for i in range(1, 51)]
        kwargs = dict({'mode': 'synthesis',
                       'theory': 'cpp',
                       'program_lines': 13,
                       'program': 'miconic.prog',
                       'num_extra_pointers': 1,
                       'output_dir': 'test_miconic/'})

        self.base_bfgp_test(domain_file=domain, problem_files=problems, args=kwargs)

        """Testing the BFGP++ solver can validate 10 last (and larger) Miconic instances"""
        domain = 'domains/miconic/domain.pddl'
        problems = [f'domains/miconic/training/easy/p{i:02}.pddl' for i in range(90, 100)]
        kwargs = dict({'mode': 'validation-prog',
                       'theory': 'cpp',
                       'program': 'miconic.prog',
                       'num_extra_pointers': 1,
                       'output_dir': 'test_miconic/'})

        self.base_bfgp_test(domain_file=domain, problem_files=problems, args=kwargs)

    """
    # ToDo: update the theory to capture goals in the initial state
    def test_bfgp_satellite(self):
        # Testing the BFGP++ solver can solve 20 first Satellite instances
        domain = 'domains/satellite/domain.pddl'
        problems = [f'domains/satellite/training/easy/p{i:02}.pddl' for i in range(1, 21)]
        kwargs = dict({'mode': 'synthesis',
                       'theory': 'cpp',
                       'program_lines': 15,
                       'program': 'satellite.prog',
                       'num_extra_pointers': 1,
                       'output_dir': 'test_satellite/'})

        self.base_bfgp_test(domain_file=domain, problem_files=problems, args=kwargs)

        # Testing the BFGP++ solver can validate 10 last (and larger) Spanner instances
        domain = 'domains/satellite/domain.pddl'
        problems = [f'domains/satellite/training/easy/p{i:02}.pddl' for i in range(90, 100)]
        kwargs = dict({'mode': 'validation-prog',
                       'theory': 'cpp',
                       'program': 'satellite.prog',
                       'num_extra_pointers': 1,
                       'output_dir': 'test_satellite/'})

        self.base_bfgp_test(domain_file=domain, problem_files=problems, args=kwargs)
    """


if __name__ == "__main__":
    unittest.main()
