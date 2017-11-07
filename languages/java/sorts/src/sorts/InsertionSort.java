package sorts;

import java.util.ArrayList;
import java.util.List;

public class InsertionSort extends Sort {
    private int swaps = 0;
    private int comps = 0;


    public void sort(List<Integer> a, Boolean debug) {
        List<Integer> array = new ArrayList<Integer>(a);
        System.out.println("Insertion sort");
        for (int i = 1; i < array.size(); i++) {
            for (int j = i; j > 0; j--) {
                if (array.get(j) < array.get(j-1)) {
                    swap(array, j, j-1);
                    this.swaps++;
                }
                this.comps++;
            }
        }
        printCost(debug, this.swaps, this.comps);
        printSortedArray(array);
    }
}
