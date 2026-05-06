#include <stdio.h>
int main() {
    int a = 1, b = 1, c = 1; 
    b = (++a, b++, a++); 
    c = a + b +c; 
    printf("%d", c); 
}