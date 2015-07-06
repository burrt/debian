/* Divides the array up by 2 until you have single elements
 * Then you begin to merge them into a sorted array of size 2*n
 * And eventually as you combine these split arrays, it will be sorted
 */
 
#define min(A,B) (A<B ? A : B)
int merge (int a[], int l, int m, int r);

void mergesortBU (int a[], int l, int r)
{ 
    int i, m, end;
    for (m = 1; m <= r-l; m = 2*m) 
    {
        for (i = l; i <= r-m; i += 2*m) 
        {
            end = min(i + 2*m – 1, r));
            merge (a, i, i+m-1, end);
        }
    }
}
