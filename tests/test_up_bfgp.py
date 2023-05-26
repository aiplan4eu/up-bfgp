from unified_planning.shortcuts import *  # type: ignore
from unified_planning.io import PDDLReader
from collections import namedtuple  # type: ignore
from unified_planning.plans import PlanKind  # type: ignore
import unittest
from unified_planning.engines.results import PlanGenerationResultStatus
import up_bfgp


class BFGPtest(unittest.TestCase):
    def test_bfgp(self):
        """Testing the BFGP++ solvers can solve 3 different Gripper instances"""

    with up.environment.get_environment().factory.FewshotPlanner(name='bfgp') as bfgp:
        bfgp.set_arguments(program_lines=15)
        # Read the 3 gripper problems in the test
        pddl_problems = [PDDLReader().parse_problem('gripper/domain.pddl', f'gripper/p0{idx}.pddl') for idx in range(1, 4)]
        # Compute the generalized plan for these 3 problems
        result = bfgp.solve(pddl_problems, output_stream=sys.stdout)
        # Check whether all generated plans are satisficing
        if all(r == PlanGenerationResultStatus.SOLVED_SATISFICING for r in result):
            print(f'{bfgp.name} found a valid generalized plan!')
            # print(f'The plan is:')
            # print('\n'.join(str(x) for x in result.plan.actions))
        else:
            print('No generalized plan found!')


if __name__ == "__main__":
    unittest.main()
