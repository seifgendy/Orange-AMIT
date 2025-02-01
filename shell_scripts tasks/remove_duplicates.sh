#!/bin/bash

# Prompt the user for the filename
echo "Enter the filename:"
read filename

# Remove duplicate lines and save to a new file
sort "$filename" | uniq > "${filename}_no_duplicates.txt"

echo "Duplicate lines removed. Check the file '${filename}_no_duplicates.txt'."