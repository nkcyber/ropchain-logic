// https://docs.pwntools.com/en/stable/elf/corefile.html#using-corefiles-to-automate-exploitation
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

void win() {
	printf("you got the shell!\nHere is the flag: ");
    char buffer[256];
    FILE *fp = fopen("flag.txt", "r");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return;
    }
    if (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }
    fclose(fp);
}

void bof(char* input) {
	char buffer[64];
	strcpy(buffer, input);
}

int main(int argc, char** argv) {
	puts("welcome!");
	bof(argv[1]);
}
