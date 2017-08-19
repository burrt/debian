#!/usr/bin/env python2.7


if __name__ == "__main__":
    import sys

    # This waits (blocks) until there is input
    # Optionally, we can provide text
    for i in xrange(0, 3):
        input = raw_input("Waiting for input:")
        print "Echo input: %s" % (input)


    # This waits until stdin is terminated
    print "\nTerminate with Ctrl+D when you're done."
    input = sys.stdin.readlines()
    print "\nYour input:"
    for line in input:
        print line.rstrip()
