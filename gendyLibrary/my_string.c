#include "my_string.h"  

int str_length(const char *str) 
{
    int counter = 0;
    while (str[counter] != '\0') {
        counter++;
    }
    return counter;
}

int print_str(const char *str)
{
    int counter = 0;
    while (str[counter] != '\0') {
        putchar(str[counter]);  
        counter++;
    }
    putchar('\n');  
    return counter;
}


