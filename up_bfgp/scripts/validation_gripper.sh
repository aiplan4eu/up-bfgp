python bfgp.py 	-d  ../tests/domains/gripper/domain.pddl \
                -i  ../tests/domains/gripper/p01.pddl \
                    ../tests/domains/gripper/p02.pddl \
                    ../tests/domains/gripper/p03.pddl \
                -m validation-prog \
                -t cpp \
                -o tmp/ \
                -p gripper
