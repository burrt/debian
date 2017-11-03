#!/usr/bin/env python3

# Geoff
#
# Using len(l) in the loop really isn't a good idea - to be changed

import sys
import argparse


def bubble_sort(l, verbose):
    i = 0
    j = 0
    swaps = 0
    total_swaps = 0
    comps = 0
    while i < len(l) and len(l) > 1:
        while j < len(l)-1:
            if l[j] > l[j+1]:
                tmp = l[j+1]
                l[j+1] = l[j]
                l[j] = tmp
                swaps += 1
                total_swaps += 1
            j += 1
            comps += 1
        # Early exit
        if swaps == 0:
            break
        else:
            swaps = 0
        i += 1
        j = 0
    if verbose:
        print("Total comparisons: {0}".format(comps))
        print("Total swaps: {0}\n".format(total_swaps))



def insertion_sort(l, verbose):
    i = 0
    comps = 0
    swaps = 0
    while i < len(l)-1:
        j = i+1
        while j > 0:
            # Swap adjacent values
            if l[j] < l[j-1]:
                tmp = l[j-1]
                l[j-1] = l[j]
                l[j] = tmp
                swaps += 1
            j -= 1
            comps +=1
        i += 1
    if verbose:
        print("Total comparisons: {0}".format(comps))
        print("Total swaps: {0}\n".format(swaps))


def selection_sort(l, verbose):
    i = 0
    comps = 0
    swaps = 0
    while i < len(l)-1:
        min_index = i
        j = i+1
        while j < len(l):
            if l[j] < l[min_index]:
                min_index = j
            j += 1
            comps += 1
        # Swap
        tmp = l[min_index]
        l[min_index] = l[i]
        l[i] = tmp
        i += 1
        swaps += 1
    if verbose:
        print("Total comparisons: {0}".format(comps))
        print("Total swaps: {0}\n".format(swaps))


def merge_sort(l, verbose):
    comps = 0
    swaps = 0
    if verbose:
        print("Total comparisons: {0}".format(comps))
        print("Total swaps: {0}\n".format(swaps))



if __name__ == "__main__":

    # Create an arg parser for fun
    parser = argparse.ArgumentParser(description="Sorts a reversed list - specify the sorting algorithm.")
    # Allow user to specify what sort they want
    parser.add_argument("sort_type",
                        help="bubble, insertion, selection, merge")
    parser.add_argument("-v", "--verbosity", action="store_true",
                        help="increase output verbosity")
    args = parser.parse_args()

    # Generate an unsorted list
    l = list(reversed(range(0, 40)))
    print("Unsorted list: \n{0}\n".format(l))

    if args.sort_type == "bubble":
        print("\nBubble sort!\n{0}".format("-"*30))
        bubble_sort(l, args.verbosity)
    elif args.sort_type == "insertion":
        print("\nInsertion sort!\n{0}".format("-"*30))
        insertion_sort(l, args.verbosity)
    elif args.sort_type == "selection":
        print("\nSelection sort!\n{0}".format("-"*30))
        selection_sort(l, args.verbosity)
    else:
        print("Unknown selection sort - exiting...")
        sys.exit()

    print("Sorted list: \n{0}\n".format(l))
