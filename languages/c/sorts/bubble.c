#include <stdio.h>
#include <stdbool.h>

void print_array(int array[], int len);
void bubble_sort_no_ee(int array[], int len);
void bubble_sort_ee(int array[], int len);


// No early exit
// O(n^2)
void bubble_sort_no_ee(int array[], int len)
{
    int temp;
    int comps = 0;
    for (int i = 0; i < len; i++)
    {
        printf("Phase: %d\n", i);
        for (int j = 1; j < len; j++)
        {
            if (array[j] < array[j-1])
            {
                temp = array[j-1];
                array[j-1] = array[j];
                array[j] = temp;
                print_array(array, len);
            }
            comps++;
            print_array(array, len);
        }
    }
    printf("Comparisons = %d\n", comps);
}


// Early exit
// Best case still (n-1)
// O(n^2)
void bubble_sort_ee(int array[], int len)
{
    int temp;
    int done = true;
    int comps = 0;
    for (int i = 0; i < len; i++)
    {
        done = true;
        printf("Phase: %d\n", i);
        for (int j = 1; j < len; j++)
        {
            comps++;
            if (array[j] < array[j-1])
            {
                temp = array[j-1];
                array[j-1] = array[j];
                array[j] = temp;
                print_array(array, len);
                done = false;
            }
        }
        if (done)
        {
            printf("Comparisons (EE) = %d\n", comps);
            return;
        }
    }
    printf("Comparisons = %d\n", comps);
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
    int array[LEN] = {6, 5, 4, 1, 2, 3};
    //int array[LEN] = {1, 2, 3, 4, 5, 6};

    if (argc == 2 && argv[1][0] == 'e')
    {
        bubble_sort_ee(array, LEN);
    }
    else
    {
        bubble_sort_no_ee(array, LEN);
    }

    printf("\nSorted array:\n");
    print_array(array, LEN);


    return 0;
}
