void swap (int a, int b, int *items[]) 
{
    int temp = items[a];
    items[a] = items[b];
    items[b] = temp;
}

/* Without early exit
 */
void bubbleSort (int items[], int n) 
{
    int i, j;
    for (i = n - 1; i > 0 ; i--)
    {
        for (j = 1; j <= i; j++)
        {
            if (items[j-1] > items[j])
            {
                swap(j, j-1, &items); // something like this 
            }
        }
    }
}

/* With early exit - adaptive
 */
void bubbleSortEE (int items[], int n) 
{
    int i, j;
    int done = 0;
    for (i = n - 1; i > 0 && !done; i--) // break if there was no swap in the phase
    {
        done = 1;
        for (j = 1; j <= i; j++) 
        {
            if (items[j - 1] > items[j]) 
            {
                swap(j, j - 1,items);
                done = 0;
            }
        }
    }
}
