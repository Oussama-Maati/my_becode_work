#!/bin/bash

path="$1"

if [ -f "$path" ]; then
    ext="${path##*.}"
    case "$ext" in
        txt|js)
            cat "$path";;
        *)
            echo "Error: Unsupported file type."
    esac
elif [ -d "$path" ]; then
    ls -l "$path"
else
    echo "Error: Invalid path."
fi
