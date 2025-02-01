#!/bin/bash

# Prompt the user for input
echo "Enter a number (N):"
read N

# Initialize sum
sum=0

# Loop to calculate the sum
for (( i=1; i<=N; i++ ))
do
    sum=$((sum + i))
done

# Output the result
echo "The sum of integers from 1 to $N is: $sum"