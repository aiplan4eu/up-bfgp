# All OK!
python bfgp.py -d bfgp_pp/domains/gripper/synthesis/domain.pddl \
               -i bfgp_pp/domains/gripper/synthesis/p01.pddl \
                  bfgp_pp/domains/gripper/synthesis/p02.pddl \
                  bfgp_pp/domains/gripper/synthesis/p03.pddl \
               -m repair \
               -t cpp \
               -l 10 \
               -f ed ilc \
               -o tmp_ok/ \
               -p bfgp_pp/program_repair/strips/gripper/gripper_cpp_ok
               
# Missing loops
python bfgp.py -d bfgp_pp/domains/gripper/synthesis/domain.pddl \
               -i bfgp_pp/domains/gripper/synthesis/p01.pddl \
                  bfgp_pp/domains/gripper/synthesis/p02.pddl \
                  bfgp_pp/domains/gripper/synthesis/p03.pddl \
               -m repair \
               -t cpp \
               -l 10 \
               -f ed ilc \
               -o tmp_missing_loops/ \
               -p bfgp_pp/program_repair/strips/gripper/gripper_cpp_missing_loops

# Missing planning actions
python bfgp.py -d bfgp_pp/domains/gripper/synthesis/domain.pddl \
               -i bfgp_pp/domains/gripper/synthesis/p01.pddl \
                  bfgp_pp/domains/gripper/synthesis/p02.pddl \
                  bfgp_pp/domains/gripper/synthesis/p03.pddl \
               -m repair \
               -t cpp \
               -l 10 \
               -f ed ilc \
               -o tmp_missing_planning_actions/ \
               -p bfgp_pp/program_repair/strips/gripper/gripper_cpp_missing_planning_actions
