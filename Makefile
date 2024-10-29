CC=gcc
CFLAGS=-g -Wall -Werror

all: example

example: example.o
	$(CC) $(CFLAGS) -o $@ $^

example.o: example.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f example example.o
