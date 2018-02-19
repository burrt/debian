"""
Author: Geoff

Some sorthing algorithms for fun!
If you spot an error - report them please!
"""

import argparse
import logging
from random import randint


description = """Sorts a reversed list - specify the sorting algorithm:
              bubble,
              insertion,
              selection,
              merge,
              quick - haore partition,
              quick - lomuto partition
              """


def swap(arr, x, y):
    global swaps
    tmp = arr[x]
    arr[x] = arr[y]
    arr[y] = tmp
    swaps += 1


def print_info_reset():
    global comps
    global swaps
    print("Total comparisons: {0}".format(comps))
    print("Total swaps: {0}\n".format(swaps))
    swaps = 0
    comps = 0


def bubble_sort(arr):
    """Bubble sort with early exit"""
    global comps
    n = len(arr)
    ee_swaps = 0
    comps = 0
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
                ee_swaps += 1
            comps += 1
        # early exit
        if ee_swaps == 0:
            break
        else:
            ee_swaps = 0
        n -= 1


def insertion_sort(arr):
    global comps
    n = len(arr)
    for i in range(n-1):
        j = i+1
        while j > 0:
            # swap adjacent values
            if arr[j] < arr[j-1]:
                swap(arr, j, j-1)
            j -= 1
            comps += 1


def selection_sort(arr):
    """Selection sort"""
    global comps
    n = len(arr)
    for i in range(n-1):
        min_index = i
        j = i+1
        for j in range(j, n):
            if arr[j] < arr[min_index]:
                min_index = j
            comps += 1
        # swap the smallest val on the RHS with current key
        if min_index != i:
            swap(arr, min_index, i)


def merge_sort(arr):
    """Merge sort"""
    global comps
    n = len(arr)
    if n > 1:
        mid = n//2  # floor division for python 3
        left = arr[:mid]
        right = arr[mid:]
        logging.info("Split list\nLeft: {0}\nRight:{1}\n".format(left, right))

        # recursively call merge_sort on the split lists
        merge_sort(left)
        merge_sort(right)

        # at this point we have hit a leaf node and returned
        # we need to merge the two lists left, right
        i = 0  # parent list
        x = 0  # left index
        y = 0  # right index
        while x < len(left) and y < len(right):
            if left[x] <= right[y]:
                arr[i] = left[x]
                x += 1
            else:
                arr[i] = right[y]
                y += 1
            i += 1
            comps += 1

        # depending on which split list finished first
        # we override with the left-over
        if x < len(left):
            arr[i:] = left[x:]
        if y < len(right):
            arr[i:] = right[y:]
        logging.info("Merged: {0}\n".format(arr))


def quick_sort(arr, lo, hi, scheme):
    """Quick sort with different partition schemes - Lomuto, Hoare"""

    def lomuto_partition(l_arr, lo, hi):
        global comps
        pivot = l_arr[hi]
        i = lo-1
        j = lo
        while j < hi:
            if l_arr[j] < pivot:
                i += 1
                swap(l_arr, i, j)
            comps += 1
            j += 1
        swap(l_arr, i+1, hi)
        comps += 1
        return i+1

    def hoare_partition(h_arr, lo, hi):
        global comps
        pivot = h_arr[lo]
        i = lo-1
        j = hi+1
        while True:
            i += 1  # emulate do while
            while h_arr[i] < pivot:
                i += 1
                comps += 1
            j -= 1  # emulate do while
            while h_arr[j] > pivot:
                j -= 1
                comps += 1
            if i >= j:
                comps += 1
                return j
            swap(h_arr, i, j)

    # start of quick sort
    if lo < hi:
        if scheme == "quick_l":
            p = lomuto_partition(arr, lo, hi)
            quick_sort(arr, lo, p-1, scheme)
        else:
            p = hoare_partition(arr, lo, hi)
            quick_sort(arr, lo, p, scheme)
        quick_sort(arr, p+1, hi, scheme)


if __name__ == "__main__":
    # use some dirty globals for swaps and comps to make life easy
    swaps = 0
    comps = 0

    # create an arg parser for fun
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
    unsorted_list = [randint(0, 100) for _ in range(20)]
    print("Unsorted list:\n{0}\n{1}\n".format(80*"-", unsorted_list))

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
        assert(sorted_list == sorted(unsorted_list))
        print("Sorted list: \n{0}\n{1}\n".format(80*"-", sorted_list))
