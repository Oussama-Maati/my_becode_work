#!/bin/bash

current_date=$(date +"%Y-%m-%d")
current_time=$(date +"%H:%M:%S")
username=$(whoami)
current_directory=$(pwd)

echo "Date: $current_date"
echo "Time: $current_time"
echo "Username: $username"
echo "Directory: $current_directory"
