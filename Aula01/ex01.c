#include <stdio.h>
int main() {
   int var1 = 3;
   printf("%p %i %i\n ", &var1, var1, *var1);
   return 0;
}
