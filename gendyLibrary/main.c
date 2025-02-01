//   gcc my_string.c main.c -o my_program

//   ./my_program



/*
# Compile source files into object files
gcc -c my_string.c -o my_string.o
gcc -c main.c -o main.o

# Create the static library
ar rcs libmystring.a my_string.o

# Link the static library with the main program
gcc main.o -L. -lmystring -o my_program

# Run the program
./my_program

*/








#include "my_string.h"

int main()
{
    print_str("Hello, World!\n");
    return 0;
}




