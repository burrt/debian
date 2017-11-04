#!/usr/bin/env python3

# Geoff
#
# Using len(l) in the loop really isn't a good idea - to be changed

import sys
import argparse
import logging


def swap(l, x, y):
    tmp = l[x]
    l[x] = l[y]
    l[y] = tmp


def bubble_sort(l):
    i = 0
    j = 0
    swaps = 0
    total_swaps = 0
    comps = 0
    while i < len(l) and len(l) > 1:
        while j < len(l)-1:
            if l[j] > l[j+1]:
                swap(l, j, j+1)
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
    logging.info("Total comparisons: {0}".format(comps))
    logging.info("Total swaps: {0}\n".format(total_swaps))



def insertion_sort(l):
    i = 0
    comps = 0
    swaps = 0
    while i < len(l)-1:
        j = i+1
        while j > 0:
            # Swap adjacent values
            if l[j] < l[j-1]:
                swap(l, j, j-1)
                swaps += 1
            j -= 1
            comps +=1
        i += 1
    logging.info("Total comparisons: {0}".format(comps))
    logging.info("Total swaps: {0}\n".format(swaps))


def selection_sort(l):
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
        # Swap the smallest val on the RHS with current key
        if min_index != i:
            swap(l, min_index, i)
            swaps += 1
        i += 1
    logging.info("Total comparisons: {0}".format(comps))
    logging.info("Total swaps: {0}\n".format(swaps))


def merge_sort(l):
    comps = 0
    swaps = 0
    if len(l) > 1:
        mid = len(l)//2 # floor division for python 3
        left = l[:mid]
        right = l[mid:]
        logging.info("Split list\nLeft: {0}\nRight:{1}\n".format(left, right))

        # Recursively call merge_sort on the split lists
        merge_sort(left)
        merge_sort(right)

        # At this point we have hit a leaf node and returned
        # We need to merge the two lists left, right
        i = 0 # parent list
        x = 0 # left index
        y = 0 # right index
        while x < len(left) and y < len(right):
            if left[x] <= right[y]:
                l[i] = left[x]
                x += 1
            else:
                l[i] = right[y]
                y += 1
            i += 1

        # Depending on which split list finished first, we override with the left-over
        if x < len(left):
            l[i:] = left[x:]
        if y < len(right):
            l[i:] = right[y:]
        logging.info("Merged: {0}\n".format(l))




if __name__ == "__main__":

    # Create an arg parser for fun
    parser = argparse.ArgumentParser(description="Sorts a reversed list - specify the sorting algorithm.")
    # Allow user to specify what sort they want
    parser.add_argument("sort_type",
                        help="bubble, insertion, selection, merge")
    parser.add_argument("-v", "--verbosity", action="store_true",
                        help="increase output verbosity")
    args = parser.parse_args()

    # Create a very basic logger
    if args.verbosity:
        logger = logging.basicConfig(level=logging.INFO)


    # Generate an unsorted list
    l = list(reversed(range(0, 10)))
    print("Unsorted list: \n{0}\n".format(l))

    if args.sort_type == "bubble":
        print("Bubble sort!\n{0}\n".format("-"*30))
        bubble_sort(l)
    elif args.sort_type == "insertion":
        print("Insertion sort!\n{0}\n".format("-"*30))
        insertion_sort(l)
    elif args.sort_type == "selection":
        print("Selection sort!\n{0}\n".format("-"*30))
        selection_sort(l)
    elif args.sort_type == "merge":
        print("Merge sort!\n{0}\n".format("-"*30))
        merge_sort(l)
    else:
        print("Unknown selection sort - exiting...")
        sys.exit()

    print("Sorted list: \n{0}\n".format(l))
