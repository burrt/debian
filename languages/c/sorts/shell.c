/*
 */
void shellsort (int items[], int n) 
{
    int i, j, h;
    
    //the starting size of h is found.
    for (h = 1; h <= (n - 1)/9; h = (3 * h) + 1);    
    
    for (; h > 0; h /= 3) 
    {
        //This inner loop is just like simple insertion sort when h is 1
        for (i = h; i < n; i++) 
        {
            int key = items[i];
            for(j=i; j >= h && key < items[j - h]; j -=h)
            {
                items[j] = items[j - h];
            }
            items[j] = key;
        }
    }
}
