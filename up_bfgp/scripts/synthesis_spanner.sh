python bfgp.py 	-d  ../tests/domains/spanner/domain.pddl \
				-i 	../tests/domains/spanner/training/easy/p01.pddl \
					../tests/domains/spanner/training/easy/p02.pddl \
					../tests/domains/spanner/training/easy/p03.pddl \
					../tests/domains/spanner/training/easy/p04.pddl \
					../tests/domains/spanner/training/easy/p05.pddl \
					../tests/domains/spanner/training/easy/p06.pddl \
					../tests/domains/spanner/training/easy/p07.pddl \
					../tests/domains/spanner/training/easy/p08.pddl \
					../tests/domains/spanner/training/easy/p09.pddl \
					../tests/domains/spanner/training/easy/p10.pddl \
				-m synthesis \
				-t  cpp \
				-l 16 \
				-p spanner
