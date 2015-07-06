/* Adaptive, in-place
 * Find the min item in array
 * Swap it with the first value in the array
 * Repeat as you move to the RHS
 *
 * eg
 * 66 25 12 22 11 // 11 is smallest, swap with first
 * 11 25 12 22 66 // 12 is smallest, swap with second
 * 11 12 25 22 66 // ..
 * 11 12 22 25 66
 * 11 12 22 25 66
 */
void selection_sort (int items[], int n) 
{
    int i, j, min;
    for (i = 0; i < n-1; i++) 
    {
        min = i; // current minimum is first unsorted element
                 // find index of minimum element
        for (j = i+1; j < n; j++)
        {
            if (items[j] < items[min])
                min = j;
        }
        // swap minimum element into place
        swap (i, min, items[i], items[min]);
    }
}
