# Geoff
# Using len(l) in the loop really isn't a good idea - to be changed

import sys
import argparse
import logging


description = """Sorts a reversed list - specify the sorting algorithm:
              insertion,
              selection,
              merge,
              quick - haore partition,
              quick - lomuto partition
              """


def swap(l, x, y):
    global swaps
    tmp = l[x]
    l[x] = l[y]
    l[y] = tmp
    swaps += 1


def print_info_reset():
    global comps
    global swaps
    print("Total comparisons: {0}".format(comps))
    print("Total swaps: {0}".format(swaps))
    swaps = 0
    comps = 0


def bubble_sort(l):
    """Bubble sort with early exit"""
    global comps
    i = 0
    j = 0
    ee_swaps = 0
    comps = 0
    while i < len(l) and len(l) > 1:
        while j < len(l)-1:
            if l[j] > l[j+1]:
                swap(l, j, j+1)
                ee_swaps += 1
            j += 1
            comps += 1
        # Early exit
        if ee_swaps == 0:
            break
        else:
            ee_swaps = 0
        i += 1
        j = 0


def insertion_sort(l):
    global comps
    i = 0
    while i < len(l)-1:
        j = i+1
        while j > 0:
            # Swap adjacent values
            if l[j] < l[j-1]:
                swap(l, j, j-1)
            j -= 1
            comps += 1
        i += 1


def selection_sort(l):
    """Selection sort"""
    global comps
    i = 0
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
        i += 1


def merge_sort(l):
    """Merge sort"""
    global comps
    if len(l) > 1:
        mid = len(l)//2  # floor division for python 3
        left = l[:mid]
        right = l[mid:]
        logging.info("Split list\nLeft: {0}\nRight:{1}\n".format(left, right))

        # Recursively call merge_sort on the split lists
        merge_sort(left)
        merge_sort(right)

        # At this point we have hit a leaf node and returned
        # We need to merge the two lists left, right
        i = 0  # parent list
        x = 0  # left index
        y = 0  # right index
        while x < len(left) and y < len(right):
            if left[x] <= right[y]:
                l[i] = left[x]
                x += 1
            else:
                l[i] = right[y]
                y += 1
            i += 1
            comps += 1

        # Depending on which split list finished first, we override with the left-over
        if x < len(left):
            l[i:] = left[x:]
        if y < len(right):
            l[i:] = right[y:]
        logging.info("Merged: {0}\n".format(l))


def quick_sort(l, lo, hi, scheme):
    """Quick sort with different partition schemes"""

    def lomuto_partition(l, lo, hi):
        global comps
        pivot = l[hi]
        i = lo-1
        j = lo
        while j < hi:
            if l[j] < pivot:
                i += 1
                swap(l, i, j)
            comps += 1
            j += 1
        if l[hi] < l[i+1]:
            swap(l, i+1, hi)
        comps += 1
        return i+1

    def hoare_partition(l, lo, hi):
        global comps
        pivot = l[lo]
        i = lo  # emulate do while
        j = hi  # emulate do while
        while True:
            while l[i] < pivot:
                i += 1
                comps += 1
            while l[j] > pivot:
                j -= 1
                comps += 1
            if i >= j:
                comps += 1
                return j
            swap(l, i, j)

    # Start of quick sort
    if lo < hi:
        if scheme == "lomuto":
            p = lomuto_partition(l, lo, hi)
            quick_sort(l, lo, p-1, scheme)
        else:
            p = hoare_partition(l, lo, hi)
            quick_sort(l, lo, p, scheme)
        quick_sort(l, p+1, hi, scheme)


if __name__ == "__main__":
    # Use some dirty globals for swaps and comps to make life easy
    swaps = 0
    comps = 0

    # Create an arg parser for fun
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-s", "--sort_type",
                        nargs='*',
                        choices=['bubble', 'insertion', 'selection',
                                 'merge', 'quick_h', 'quick_l'],
                        default=['merge'],
                        help="bubble, insertion, selection, merge, quick_h, quick_l")
    parser.add_argument("-v", "--verbosity", action="store_true",
                        help="increase output verbosity")
    args = parser.parse_args()

    # create a very basic logger
    if args.verbosity:
        logger = logging.basicConfig(level=logging.INFO)

    # generate a reversed list
    unsorted_list = list(reversed(range(0, 10)))
    print("Unsorted list:\n{0}\n{1}\n".format(50*"-", unsorted_list))

    # generate a dictionary of all the functions
    sorts = {'bubble': bubble_sort,
             'insertion': insertion_sort,
             'selection': selection_sort,
             'merge': merge_sort,
             'quick_h': quick_sort,
             'quick_l': quick_sort}

    for s in args.sort_type:
        # create a copy of the list since the sorts are in-place
        sorted_list = unsorted_list[:]
        print("Sorting algorithm: {0}\n{1}".format(s, 50*"-"))
        if s == 'quick_h' or s == 'quick_l':
            sorts[s](sorted_list, 0, len(unsorted_list)-1, s)
        else:
            sorts[s](sorted_list)
        print_info_reset()
        print("Sorted list: \n{0}\n".format(sorted_list))
