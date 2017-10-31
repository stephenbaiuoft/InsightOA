#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
# run this program, waiting for argument

# get script_dir for run.sh
# script_tempdir=$(pwd)
# echo "temp dir is: ${script_tempdir}"

python ./src/find_political_donors.py ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt

