/* Worst case performance    О(n^2) comparisons, swaps
 * Best case performance     O(n) comparisons, O(1) swaps
 * Average case performance  О(n^2) comparisons, swaps
 * 
 * Select the element, check the LHS of the array and drop it in place
 * As you move to the RHS of the array, the more comparisons/swaps you make
 *
 * eg
 * Pass 1
 * 5 (4) 3 2 1 ⟶ (4) 5 3 2 1
 * Pass 2
 * 4 5 (3) 2 1 ⟶ 4 (3) 5 2 1 ⟶ (3) 4 5 2 1
 * Pass 3
 * 3 4 5 (2) 1 ⟶ 3 4 (2) 5 1⟶ 3 (2) 4 5 1 ⟶ (2) 3 4 5 1
 * Pass 4
 * 2 3 4 5 (1) ⟶ 2 3 4 (1) 5 ⟶ 2 3 (1) 4 5 ⟶ 2 (1) 3 4 5 ⟶ (1) 2 3 4 5
 */
void insertion_sort (int *a, int n)
{
    int tmp, i, j;
    for (i = 1; i < n; ++i)             // start from the second element
    {
        tmp = a[i];                     // and eventually move to the right of the array[i++]
        j = i;
        while (j > 0 && tmp < a[j - 1]) // compare adjacent array contents initially
        {   
            a[j] = a[j - 1];            // then compare all values leading up to array[j-1] ie. compare all values to the left
            --j;                        // the j>0 allows the comparison of a[0] since a[j-1] i.e a[0] !
        }
        a[j] = tmp;
    }
}


/* Alternative
 */
void insertion_sort (int items[], int n) 
{
    int i, j, key;
    for (i = 1; i <= n; i++) 
    {
        key = items[i];
        for (j = i; j > 0 && key < items[j-1]; j--)
        {
            items[j] = items[j - 1];
        }
        items[j] = key;
    }
}
