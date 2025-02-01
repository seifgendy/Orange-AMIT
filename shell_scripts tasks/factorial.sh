#!/bin/bash

# Function to calculate factorial
factorial() {
    local num=$1
    local result=1

    for (( i=1; i<=num; i++ ))
    do
        result=$((result * i))
    done

    echo $result
}

# Prompt the user for input
echo "Enter a number:"
read number

# Call the factorial function
echo "The factorial of $number is: $(factorial $number)"