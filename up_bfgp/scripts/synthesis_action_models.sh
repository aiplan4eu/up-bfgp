python bfgp.py -d ../tests/domains/action_models/gripper/pick/domain.txt \
               -i ../tests/domains/action_models/gripper/pick/1.txt \
                  ../tests/domains/action_models/gripper/pick/2.txt \
                  ../tests/domains/action_models/gripper/pick/3.txt \
                  ../tests/domains/action_models/gripper/pick/4.txt \
                  ../tests/domains/action_models/gripper/pick/5.txt \
                  ../tests/domains/action_models/gripper/pick/6.txt \
                  ../tests/domains/action_models/gripper/pick/7.txt \
                  ../tests/domains/action_models/gripper/pick/8.txt \
                  ../tests/domains/action_models/gripper/pick/9.txt \
                  ../tests/domains/action_models/gripper/pick/10.txt \
                  ../tests/domains/action_models/gripper/pick/11.txt \
                  ../tests/domains/action_models/gripper/pick/12.txt \
                  ../tests/domains/action_models/gripper/pick/13.txt \
                  ../tests/domains/action_models/gripper/pick/14.txt \
                  ../tests/domains/action_models/gripper/pick/15.txt \
                  ../tests/domains/action_models/gripper/pick/16.txt \
                  ../tests/domains/action_models/gripper/pick/17.txt \
                  ../tests/domains/action_models/gripper/pick/18.txt \
                  ../tests/domains/action_models/gripper/pick/19.txt \
                  ../tests/domains/action_models/gripper/pick/20.txt \
               -m synthesis \
               -t actions_strips \
               -f ilc mi cwed \
               -p gripper_pick


python bfgp.py -d ../tests/domains/action_models/elevators/stop/domain.txt \
               -i ../tests/domains/action_models/elevators/stop/1.txt \
                  ../tests/domains/action_models/elevators/stop/2.txt \
                  ../tests/domains/action_models/elevators/stop/3.txt \
                  ../tests/domains/action_models/elevators/stop/4.txt \
                  ../tests/domains/action_models/elevators/stop/5.txt \
                  ../tests/domains/action_models/elevators/stop/6.txt \
                  ../tests/domains/action_models/elevators/stop/7.txt \
                  ../tests/domains/action_models/elevators/stop/8.txt \
                  ../tests/domains/action_models/elevators/stop/9.txt \
                  ../tests/domains/action_models/elevators/stop/10.txt \
                  ../tests/domains/action_models/elevators/stop/11.txt \
                  ../tests/domains/action_models/elevators/stop/12.txt \
                  ../tests/domains/action_models/elevators/stop/13.txt \
                  ../tests/domains/action_models/elevators/stop/14.txt \
                  ../tests/domains/action_models/elevators/stop/15.txt \
                  ../tests/domains/action_models/elevators/stop/16.txt \
                  ../tests/domains/action_models/elevators/stop/17.txt \
                  ../tests/domains/action_models/elevators/stop/18.txt \
                  ../tests/domains/action_models/elevators/stop/19.txt \
                  ../tests/domains/action_models/elevators/stop/20.txt \
               -m synthesis \
               -t actions_adl \
               -l 18 \
               -f ilc mi cwed \
               -p elevators_stop

python bfgp.py -d ../tests/domains/action_models/rule90/domain.txt \
               -i ../tests/domains/action_models/rule90/1.txt \
                  ../tests/domains/action_models/rule90/2.txt \
                  ../tests/domains/action_models/rule90/3.txt \
                  ../tests/domains/action_models/rule90/4.txt \
                  ../tests/domains/action_models/rule90/5.txt \
                  ../tests/domains/action_models/rule90/6.txt \
                  ../tests/domains/action_models/rule90/7.txt \
                  ../tests/domains/action_models/rule90/8.txt \
                  ../tests/domains/action_models/rule90/9.txt \
                  ../tests/domains/action_models/rule90/10.txt \
                  ../tests/domains/action_models/rule90/11.txt \
                  ../tests/domains/action_models/rule90/12.txt \
                  ../tests/domains/action_models/rule90/13.txt \
                  ../tests/domains/action_models/rule90/14.txt \
                  ../tests/domains/action_models/rule90/15.txt \
                  ../tests/domains/action_models/rule90/16.txt \
                  ../tests/domains/action_models/rule90/17.txt \
                  ../tests/domains/action_models/rule90/18.txt \
                  ../tests/domains/action_models/rule90/19.txt \
                  ../tests/domains/action_models/rule90/20.txt \
               -m synthesis \
               -t actions_cell \
               -l 95 \
               -s 2 \
               -f ilc mi cwed \
               -p cell_rule90

python bfgp.py -d ../tests/domains/action_models/pancakes/domain.txt \
               -i ../tests/domains/action_models/pancakes/1.txt \
                  ../tests/domains/action_models/pancakes/2.txt \
                  ../tests/domains/action_models/pancakes/3.txt \
                  ../tests/domains/action_models/pancakes/4.txt \
                  ../tests/domains/action_models/pancakes/5.txt \
                  ../tests/domains/action_models/pancakes/6.txt \
                  ../tests/domains/action_models/pancakes/7.txt \
                  ../tests/domains/action_models/pancakes/8.txt \
                  ../tests/domains/action_models/pancakes/9.txt \
                  ../tests/domains/action_models/pancakes/10.txt \
                  ../tests/domains/action_models/pancakes/11.txt \
                  ../tests/domains/action_models/pancakes/12.txt \
                  ../tests/domains/action_models/pancakes/13.txt \
                  ../tests/domains/action_models/pancakes/14.txt \
                  ../tests/domains/action_models/pancakes/15.txt \
                  ../tests/domains/action_models/pancakes/16.txt \
               -m synthesis \
               -t actions_ram \
               -l 8 \
               -s 1 \
               -f ilc mi cwed \
               -p pancakes_flip