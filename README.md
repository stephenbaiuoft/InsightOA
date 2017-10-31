# Dependency
1. make sure __init __.py is included in src

# Python Run Environment
1. python 3.6
2. import sys module
3. import time module
4. from HelperModule import InputProcessor ==> This is my custom helper class

# Run Instruction
1. run the run_tests.sh script, which is under the specified project structure

# Other Note
1. the custom round_up function is necessary because Python 3.x version, round() actually rounds to the closest even number: i.e. round(2.5) == round(1.5) == 2

# Code Design
MedianQueue Class: the custom designed structure that retrieves the running median number. This class is composed of a minHeap storing numbers greater or equal to the current median and a maxHeap storing numbers smaller or equal to the current median. Whenever a new number is inserted, this number is compared to the head of minHeap and maxHeap(see code for more details). The MedianQueue automatically balances the size of minHeap and maxHeap

MedianQueue Class Time Complexity: this design ensures that insertion is O(log n) and O( const ) for retrieving the running median

InputProcessor Class: this class is responsible for parsing the data file. Only valid data entries as specified by the requirement are processed. This class uses hashmap data structures in order to find existing matches quickly(One hashmap for handling median for zip and another hashmap for handling median for date). The key is the combination of cmte and zip in the case of finding medianvals_by_zip. The key is the combination of cmte and date in the case of finding medianvals_by_date. Each key has a value of the MedianQueue structure, which is responsible for that particular key's running median. 

InputProcessor Class Time Complexity: hashing is O( const ) for searching a unique key and getting its value. 
