python bfgp.py 	-d 	../tests/domains/spanner/domain.pddl \
				-i 	../tests/domains/spanner/training/easy/p90.pddl \
					../tests/domains/spanner/training/easy/p91.pddl \
					../tests/domains/spanner/training/easy/p92.pddl \
					../tests/domains/spanner/training/easy/p93.pddl \
					../tests/domains/spanner/training/easy/p94.pddl \
					../tests/domains/spanner/training/easy/p95.pddl \
					../tests/domains/spanner/training/easy/p96.pddl \
					../tests/domains/spanner/training/easy/p97.pddl \
					../tests/domains/spanner/training/easy/p98.pddl \
					../tests/domains/spanner/training/easy/p99.pddl \
				-m validation-prog \
				-t cpp \
				-o tmp/ \
				-p spanner
