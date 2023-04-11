#!/bin/bash

# take input from user, put it in an array
# read input from the user
echo  -e "\e[0;35m Enter IDs of trackrs that you want IG_Script to collect !" 
echo  -e "\e[0;35m ---->>>> Tracker_ID1 Tracker_ID2 Tracker_ID3 ... ETC \e[0m"
read -a trackers


while true;
do

# iterate through IDs of trackers .. execute each tracker of them for 3 hours 
for tracker in "${trackers[@]}"
do

    # kill any running python processes
    pkill -f file_name.py
 
    # pass the current value as a command line arguement to IG_Script
    timeout 2s python3 cmdLineArguement.py  $tracker

    # wait for python command to finish
    wait

done

sleep 2s
# 
done