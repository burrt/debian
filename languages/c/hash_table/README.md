## Hash table

I added a simple implementation of a hash table in C.
You can either use IntelliJ's Clion and use the `CmakeLists.txt` or you can
use the included `Makefile` to build the project.

I also made some basics test cases for testing the doubly linked list
implementation in C for testing it separately.

e.g.
```
make ht
make dlinkedlist
./ht
./dlinkedlist
```

### Hash collisions

At the moment, hash collisions are resolved by separate chaining with linked
lists. Future support for open addressing and other interesting alternatives
is defenitely on the agenda!
