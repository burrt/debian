/*
  Quicksort, also known as partition-exchange sort, uses these steps:
  
  Choose any element of the array to be the pivot.
  Divide all other elements (except the pivot) into two partitions.
  All elements less than the pivot must be in the first partition.
  All elements greater than the pivot must be in the second partition.
  Use recursion to sort both partitions.
  Join the first sorted partition, the pivot, and the second sorted partition.
  
  The best pivot creates partitions of equal length (or lengths differing by 1).
  
  The worst pivot creates an empty partition (for example, if the pivot is the first or last element of a sorted array).
  
  The run-time of Quicksort ranges from O(n log n) with the best pivots, to O(n2) with the worst pivots, 
  where n is the number of elements in the array.
* Recursive
*/
void quick_sort (int a[], int l, int r)
{
   int j;
   if ( l < r ) 
   {
   	   // divide and conquer
       j = partition(a, l, r);
       quick_sort(a, l, j-1);
       quick_sort(a, j+1, r);
   }
}

int partition (int a[], int l, int r) 
{
   int pivot, i, j, t;
   pivot = a[l];
   i = l; j = r+1;
		
   while( 1)
   {
       do ++i; while( a[i] <= pivot && i <= r );
       do --j; while( a[j] > pivot );
       if( i >= j ) break;
       t = a[i]; a[i] = a[j]; a[j] = t;
   }
   t = a[l]; a[l] = a[j]; a[j] = t;
   return j;
}

void main() 
{
	int a[] = { 7, 12, 1, -2, 0, 15, 4, 11, 9};
	int i;
	printf("Unsorted array is:  ");
	for(i = 0; i < 9; ++i)
		printf(" %d ", a[i]);

	quick_sort( a, 0, 8);

	printf("\n\nSorted array is:  ");
	for(i = 0; i < 9; ++i)
		printf(" %d ", a[i]);
}



/* Alternative
 */
void quicksort (int a[], int l, int r)
{ 
    int i; 
    if (r <= l)
        return;
    i = partition (a, l, r); 
    quicksort (a, l, i-1); 
    quicksort (a, i+1, r);
}


int partition (int a[], int l, int r) 
{ 
    int i = l-1;
    int j = r; 
    int pivot = a[r]; //rightmost is pivot 
    for (;;) 
    { 
        while (a[++i] < pivot); 
        while (pivot < a[--j] && j != l);
            if (i >= j)
                break; 
            swap(i, j, a); 
    }
    swap(i, r, a); // put pivot into place 
    return i;    // index of the pivot
}





