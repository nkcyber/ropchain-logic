#include <stdio.h>
#include <string.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* void win_function(int arg1, int arg2) { */
void win_function() {
	/* printf("You won! arg1: 0x%x, arg2: 0x%x\n", arg1, arg2); */
	printf("You won!\n");
}

void vulnerable_function() {
	char buffer[32];  // Small buffer susceptible to overflow
	printf("Enter some data: ");
	fgets(buffer, 100, stdin); // improper bounds checking
}

int main() {
	printf("start...");
	vulnerable_function();
	printf("done!");
	return 0;
}


/* void rop1() { */
/* printf("ROP 1!\n"); */
/* } */

/* [> void rop2(int a) { <] */
/* void rop2() { */
/* printf("ROP 2\n"); */
/* } */

/* [> void rop3(int a, int b) { <] */
/* void rop3() { */
/* printf("ROP 3\n"); */
/* } */

/* void vulnerable(char* string) { */
/* char buffer[100]; */
/* strcpy(buffer, string); */
/* } */

/* int main(int argc, char** argv) { */
/* vulnerable(argv[1]); */
/* return 0; */
/* } */

/* #include <stdio.h> */
/* #include <stdlib.h> */

/* #define BUFFER_SIZE 100 */

/* int main() { */
/* char buffer[BUFFER_SIZE]; */
/* printf("Try to pwn me!\n"); */
/* scanf("%s", buffer); */
/* puts(buffer); */
/* return 0; */
/* } */


/* void foo() { */
/* printf("foo was called\n"); */
/* } */

/* void buffer_overflow() { */
/* char buffer[BUFFER_SIZE]; */
/* scanf("%s", buffer); */
/* printf("You entered: %s\n", buffer); */
/* } */

/* int main() { */
/* buffer_overflow(); */
/* return 0; */
/* } */

