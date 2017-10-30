#include <stdio.h>

# define LEN 6
void print_array(int array[], int len);


/* Worst case performance    О(n^2) comparisons, swaps
 * Best case performance     O(n) comparisons, O(1) swaps
 * Average case performance  О(n^2) comparisons, swaps
 */
void insertion_sort(int array[], int len)
{
    int temp;
    int comps = 0;
    int swaps = 0;
    for (int i = 1; i < len; i++)
    {
        printf("---\n");
        for (int j = i; j > 0; j--)
        {
            comps++;
            if (array[j] < array[j-1])
            {
                swaps++;
                temp = array[j-1];
                array[j-1] = array[j];
                array[j] = temp;
                print_array(array, len);
            }
        }
    }
    printf("Comparisons = %d\n", comps);
    printf("Swaps = %d\n", swaps);
}



void print_array(int array[], int len)
{
    for (int i = 0; i < len; i++)
        printf("%d, ", array[i]);
    printf("\n");
}



int main(int argc, char** argv)
{
    //int array[LEN] = {6, 5, 4, 1, 2, 3};
    //int array[LEN] = {1, 2, 3, 4, 5, 6};
    int array[LEN] = {23, 6, 3, 7, 0, 33};

    printf("Un-sorted array:\n");
    print_array(array, LEN);
    printf("\n");

    insertion_sort(array, LEN);

    printf("\nSorted array:\n");
    print_array(array, LEN);

    return 0;
}
