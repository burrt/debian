CC = gcc
CFLAGS = -Wall -Werror -O2

LIST_DIR = linked_list
HASH_DIR = hash
HASH_TABLE_DIR = hashtable

SRCS = hashtable.c


ht: hashtable.o dlinked_list_ht.o hash.o
	$(CC) $(CFLAGS) $^ -o $@

dlinkedlist: dlinked_list.o
	$(CC) $(CFLAGS) $< -o $@


hashtable.o: $(HASH_TABLE_DIR)/hashtable.c
	$(CC) $(CFLAGS) -c $< -o $@ -DHASH_TABLE

# hash function
hash.o: $(HASH_DIR)/hash.c
	$(CC) $(CFLAGS) -c $< -o $@

# doubly linked list for hash table
dlinked_list_ht.o: $(LIST_DIR)/d_linked_list.c
	$(CC) $(CFLAGS) -c $< -o $@ -DHASH_TABLE

# doubly linked list - generic
dlinked_list.o: $(LIST_DIR)/d_linked_list.c
	$(CC) $(CFLAGS) -c $< -o $@ -DLL_DEBUG


all:
	ht

clean:
	rm -f ht dlinkedlist *.o
