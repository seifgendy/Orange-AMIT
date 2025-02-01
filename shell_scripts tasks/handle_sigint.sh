#!/bin/bash

# Trap SIGINT (Ctrl+C) and execute a custom action
trap 'echo "Script interrupted by Ctrl+C. Exiting gracefully..."; exit' SIGINT

# Infinite loop to demonstrate signal handling
echo "Press Ctrl+C to interrupt the script."
while true; do
    sleep 1
done