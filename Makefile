CC=gcc
CFLAGS=-m32 -fno-stack-protector -z execstack
SOURCE=example.c
OUTPUT=example

all: 
	$(CC) $(SOURCE) $(CFLAGS) -o $(OUTPUT)

clean:
	rm -f example example.o
