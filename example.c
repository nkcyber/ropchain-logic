#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <stdbool.h>

bool allowed = false;
bool counted = false;

void allow() {
	allowed = true;
}

void count() {
	static count = 0;
	count += 1;
	if (count >= 3) {
		counted = true;
	}
}

void win() {
	if (allowed && counted) {
		puts("you got the shell! here's the flag:");
		char *args[] = {"cat", "flag.txt", NULL};
		execve("/bin/cat", args, NULL);
	}
}

void bof(char* input) {
	char buffer[64];
	strcpy(buffer, input);
}

int main(int argc, char** argv) {
	puts("welcome!");
	bof(argv[1]);
}
