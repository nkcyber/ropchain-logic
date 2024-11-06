#include <stdio.h>
#include <string.h>

void rop1() {
	printf("ROP 1!\n");
}

void rop2(int a) {
	printf("ROP 2: %x!\n", a);
}

void rop3(int a, int b) {
	printf("ROP 3: %x, %x!\n", a, b);
}

void vulnerable(char* string) {
	char buffer[100];
	strcpy(buffer, string);
}

int main(int argc, char** argv) {
	vulnerable(argv[1]);
	return 0;
}

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

