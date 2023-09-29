# All OK!
python bfgp.py -d ../tests/domains/gripper/domain.pddl \
               -i ../tests/domains/gripper/p01.pddl \
                  ../tests/domains/gripper/p02.pddl \
                  ../tests/domains/gripper/p03.pddl \
               -m repair \
               -t cpp \
               -l 10 \
               -f ed ilc \
               -o tmp_ok/ \
               -p ../tests/domains/gripper/program_repair/gripper_cpp_ok
               
# Missing loops
python bfgp.py -d ../tests/domains/gripper/domain.pddl \
               -i ../tests/domains/gripper/p01.pddl \
                  ../tests/domains/gripper/p02.pddl \
                  ../tests/domains/gripper/p03.pddl \
               -m repair \
               -t cpp \
               -l 10 \
               -f ed ilc \
               -o tmp_missing_loops/ \
               -p ../tests/domains/gripper/program_repair/gripper_cpp_missing_loops

# Missing planning actions
python bfgp.py -d ../tests/domains/gripper/domain.pddl \
               -i ../tests/domains/gripper/p01.pddl \
                  ../tests/domains/gripper/p02.pddl \
                  ../tests/domains/gripper/p03.pddl \
               -m repair \
               -t cpp \
               -l 10 \
               -f ed ilc \
               -o tmp_missing_planning_actions/ \
               -p ../tests/domains/gripper/program_repair/gripper_cpp_missing_planning_actions
