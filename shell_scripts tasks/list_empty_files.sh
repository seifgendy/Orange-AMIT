#!/bin/bash

# Prompt the user for the directory
echo "Enter the directory path:"
read dir

# Find and list empty files
echo "Empty files in '$dir':"
find "$dir" -type f -empty