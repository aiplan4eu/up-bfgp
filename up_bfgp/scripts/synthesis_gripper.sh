python bfgp.py -d bfgp_pp/domains/gripper/synthesis/domain.pddl \
               -i bfgp_pp/domains/gripper/synthesis/p01.pddl \
                  bfgp_pp/domains/gripper/synthesis/p02.pddl \
                  bfgp_pp/domains/gripper/synthesis/p03.pddl \
               -m synthesis \
               -t cpp \
               -l 10 \
               -f ed ilc \
               -p gripper
