#include <stdio.h>

int main() {
   char *hello = "Hello";
   char *world = "World";
   char *b_white = "\033[46m";
   printf("%s %s, %s!", b_white, hello, world);
   return 0;
}
