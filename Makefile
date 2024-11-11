all: 
	gcc example.c -m32 -o example -fno-stack-protector

clean:
	rm -f example example.o
