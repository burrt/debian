/* /\* Adaptive, in-place */
/*  * Find the min item in array */
/*  * Swap it with the first value in the array */
/*  * Repeat as you move to the RHS */
/*  * */
/*  * eg */
/*  * 66 25 12 22 11 // 11 is smallest, swap with first */
/*  * 11 25 12 22 66 // 12 is smallest, swap with second */
/*  * 11 12 25 22 66 // .. */
/*  * 11 12 22 25 66 */
/*  * 11 12 22 25 66 */
/*  *\/ */
/* void selection_sort (int items[], int n) */
/* { */
/*     int i, j, min; */
/*     for (i = 0; i < n-1; i++) */
/*     { */
/*         min = i; // current minimum is first unsorted element */
/*                  // find index of minimum element */
/*         for (j = i+1; j < n; j++) */
/*         { */
/*             if (items[j] < items[min]) */
/*                 min = j; */
/*         } */
/*         // swap minimum element into place */
/*         swap (i, min, items[i], items[min]); */
/*     } */
/* } */

#include <stdio.h>

void print_array(int array[], int len);

void selection_sort(int array[], int len)
{
    int temp;
    int min;
    for (int i = 0; i < len-1; i++)
    {
        min = i;
        printf("Phase: %d\n", i);
        for (int j = i+1; j < len; j++)
        {
            if (array[j] < array[min])
            {
                min = j;
            }
        }
        // swap
        temp = array[i];
        array[i] = array[min];
        array[min] = temp;
        print_array(array, len);
    }
}



void print_array(int array[], int len)
{
    for (int i = 0; i < len; i++)
        printf("%d, ", array[i]);
    printf("\n");
}


# define LEN 6

int main(int argc, char** argv)
{
    int array1[LEN] = {1, 2, 3, 4, 5, 6};
    int array2[LEN] = {6, 5, 4, 1, 2, 3};
    int array3[LEN] = {23, 6, 3, 7, 0, 33};
    int *array = array3;

    if (argc == 2)
    {
        switch (argv[1][0])
        {
        case '1':
            array = array1;
            break;
        case '2':
            array = array2;
            break;
        default:
            array = array3;
            break;
        }
    }

    printf("Un-sorted array:\n");
    print_array(array, LEN);
    printf("\n");

    selection_sort(array, LEN);

    printf("\nSorted array:\n");
    print_array(array, LEN);

    return 0;
}
