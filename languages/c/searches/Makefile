CC = gcc
CFLAGS = -Wall -ansi -pedantic

# all: hello							  # run 'make all'

# Default
clobber: clean							  # removes temporary files starting with '~' and
	rm -f *~ \#*\# core					  # ending with '#'

clean:
	rm -f search *.o					  # clean out binaries


# Build rules for file targets

breadth: breadth.o						  # output : dependency list
	$(CC) -o search $<

depth: hello.o							  # output : dependency list
	$(CC) -o search $<

hello: hello.o							  # output : dependency list
	$(CC) -o search $<


# Object files
breadth.o: breadth.c
	$(CC) $(CFLAGS) -c -o $@ $<

depth.o: depth.c
	$(CC) $(CFLAGS) -c -o $@ $<
