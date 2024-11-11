// https://docs.pwntools.com/en/stable/elf/corefile.html#using-corefiles-to-automate-exploitation
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
void win() {
    system("sh");
}
int main(int argc, char** argv) {
    char buffer[64];
    strcpy(buffer, argv[1]);
}
