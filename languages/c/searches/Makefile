CC = gcc
CFLAGS = -Wall

# Default
clobber: clean							# removes temporary files starting with '~' and
	rm -f *~ \#*\#						# ending with '#'

clean:
	rm -f bfs dfs fifo_test *.o			# clean out binaries and object files


# Build rules for file targets
fifo_test: fifo_test.o fifo_queue.o
	$(CC) $(CFLAGS) fifo_test.o fifo_queue.o -o fifo_test

bfs: bfs.o fifo_queue.o
	$(CC) $(CFLAGS) bfs.o fifo_queue.o -o bfs

dfs: dfs.o fifo_queue.o					# output : dependency list
	$(CC) -o dfs $^


# Object files
fifo_test.o: fifo_test.c fifo_queue.h
	$(CC) -c fifo_test.c

bfs.o: bfs.c fifo_queue.h
	$(CC) -c bfs.c

dfs.o: dfs.c
	$(CC) $(CFLAGS) -c $@ $<

fifo_queue.o: fifo_queue.c fifo_queue.h
	$(CC) -c fifo_queue.c
