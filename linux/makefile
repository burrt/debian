=================================================================================
MAKE COMMANDS
=================================================================================

Something to add before - Usual installation of source files:
    $ ./configure --prefix=/usr # prefix is where to install it at, many other
                                # configurations to use as well: ./configure --help
    $ make
    $ make install              # better to use checkinstall ?

Now uninstalling:
    $ make uninstall            # sudo make uninstall if installed as root


Example:
    gcc –Wall –ansi –pedantic –o testintmath testintmath.c intmath.c

---------------------------------------------------------------------------------
What the "make" command does:
---------------------------------------------------------------------------------
• Preprocessing (gcc –E intmath.c > intmath.i)
- Removes preprocessor directives
- Produces: intmath.i and testintmath.i

• Compiling (gcc –S intmath.i)
- Converts to assembly language
- Produces intmath.s and testintmath.s

• Assembling (gcc –c intmath.s)
- Converts to machine language with unresolved directives
- Produces the intmath.o and testintmath.o binaries

• Linking (gcc –o testintmath testintmath.o intmath.o –lc)
- Creates machine language exectutable
- Produces the testintmath binary
---------------------------------------------------------------------------------

Example:

# Build rules for non-file targets

all:        testintmath                         # run 'make all'
clobber:    clean                               # removes temporary files starting with '~' and
    rm -f *~ \#*\# core                         # ending with '#'
clean:
    rm -f testintmath *.o                       # clean out binaries

# Build rules for file targets
testintmath: testintmath.o intmath.o            # output : dependency list
    gcc –o $@ $< intmath.o                      # gcc –o testintmath testintmath.o intmath.o
                                                # Target file: $@
                                                # First item in the dependency list: $<

testintmath.o: testintmath.c intmath.h
    gcc -Wall -ansi -pedantic -c -o $@ $<       # gcc -Wall -ansi -pedantic -c -o testintmath.o
                                                # testintmath.c

intmath.o: intmath.c intmath.h
    gcc -Wall -ansi -pedantic -c -o $@ $<       # gcc -Wall -ansi -pedantic -c -o intmath.o intmath.c
#   $(CC) $(CFLAGS) -c -o $@ $<

CC = gcc                                        # usage: $(CC) $(CFLAGS) -c -o $@ $<
# CC = cc-arm-linux-gnueabi

CFLAGS = -Wall -ansi -pedantic
# CFLAGS = -Wall -ansi -pedantic -g
# CFLAGS = -Wall -ansi -pedantic -DNDEBUG
# CFLAGS = -Wall -ansi -pedantic -pg -O3
