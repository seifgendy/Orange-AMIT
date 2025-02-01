#!/bin/bash

# Define an array
array=(3 5 7 9 11)

# Initialize sum
sum=0

# Loop through the array and calculate the sum
for num in "${array[@]}"
do
    sum=$((sum + num))
done

# Output the result
echo "The sum of the array elements is: $sum"