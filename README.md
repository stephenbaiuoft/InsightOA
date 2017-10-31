# Dependency
1. make sure _underscores_underscores_init_underscores__underscores_.py is included in src

# Python Run Environment
1. python 3.6
2. import sys module
3. import time module
4. from HelperModule import InputProcessor ==> This is my custom helper class

# Run Instruction
1. run the run_tests.sh script, which is under the specified project structure

# Other Note
1. the custom round_up function is necessary because Python 3.x version, round() actually rounds to the closest even number: i.e. round(2.5) == round(1.5) == 2