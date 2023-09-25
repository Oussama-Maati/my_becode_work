#!/bin/bash

username="$1"
groups=$(groups "$username")

IFS=' ' read -ra group_array <<< "$groups"

for group in "${group_array[@]}"; do
    echo "$username is part of the group $group."
done
