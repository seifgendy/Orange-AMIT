#!/bin/bash

# Prompt the user for the file and word
echo "Enter the filename:"
read filename
echo "Enter the word to search:"
read word

# Count occurrences of the word
count=$(grep -o -w "$word" "$filename" | wc -l)

# Output the result
echo "The word '$word' occurs $count times in the file '$filename'."