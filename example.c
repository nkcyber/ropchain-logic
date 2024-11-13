// https://docs.pwntools.com/en/stable/elf/corefile.html#using-corefiles-to-automate-exploitation
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
void win() {
    printf("got here!\n");
    system("sh");
}

void bof(char* input) {
    char buffer[64];
    strcpy(buffer, input);
}

int main(int argc, char** argv) {
    puts("welcome!");
    bof(argv[1]);
}
