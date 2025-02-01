#!/bin/bash

# Prompt the user for the directory
echo "Enter the directory path:"
read dir

# Convert all filenames to lowercase
for file in "$dir"/*; do
    if [ -f "$file" ]; then
        mv "$file" "$(echo "$file" | tr '[:upper:]' '[:lower:]')"
    fi
done

echo "All filenames in '$dir' have been converted to lowercase."