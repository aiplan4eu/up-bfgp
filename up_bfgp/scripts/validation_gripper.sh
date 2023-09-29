python bfgp.py 	-d 	bfgp_pp/domains/gripper/synthesis/domain.pddl \
				-i 	bfgp_pp/domains/gripper/synthesis/p01.pddl \
					bfgp_pp/domains/gripper/synthesis/p02.pddl \
					bfgp_pp/domains/gripper/synthesis/p03.pddl \
				-m validation-prog \
				-t cpp \
				-o tmp/ \
				-p gripper
