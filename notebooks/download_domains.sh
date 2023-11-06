# Create folders
mkdir -p domains
mkdir -p domains/gripper
mkdir -p domains/gripper/action_models
mkdir -p domains/gripper/action_models/pick
mkdir -p domains/gripper/program_repair
mkdir -p domains/sorting

dest_domains=https://raw.githubusercontent.com/aiplan4eu/up-bfgp/master/notebooks/domains

# Download Gripper - Pick action model
for i in $(seq 1 20); do
  wget $dest_domains/gripper/action_models/pick/$i.txt -O domains/gripper/action_models/pick/$i.txt;
done
wget $dest_domains/gripper/action_models/pick/domain.txt -O domains/gripper/action_models/pick/domain.txt

# Download Gripper - Program Repair
wget $dest_domains/gripper/program_repair/gripper_cpp_missing_loops.prog -O domains/gripper/program_repair/gripper_cpp_missing_loops.prog
wget $dest_domains/gripper/program_repair/gripper_cpp_missing_planning_actions.prog -O domains/gripper/program_repair/gripper_cpp_missing_planning_actions.prog
wget $dest_domains/gripper/program_repair/gripper_cpp_ok.prog -O domains/gripper/program_repair/gripper_cpp_ok.prog

# Download Gripper
for i in $(seq 1 5); do
  wget $dest_domains/gripper/p0$i.pddl -O domains/gripper/p0$i.pddl;
done
wget $dest_domains/gripper/domain.pddl -O domains/gripper/domain.pddl

# Download Sorting
for i in $(seq 1 10); do
  wget $dest_domains/sorting/$i.txt -O domains/sorting/$i.txt;
done
wget $dest_domains/sorting/domain.txt -O domains/sorting/domain.txt