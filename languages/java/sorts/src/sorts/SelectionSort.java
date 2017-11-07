package sorts;

import java.util.ArrayList;
import java.util.List;

public class SelectionSort extends Sort {
    private int swaps = 0;
    private int comps = 0;


    public void sort(List<Integer> a, Boolean debug) {
        System.out.println("Selection sort");
        List<Integer> array = new ArrayList<Integer>(a);

        for (int i = 0; i < array.size(); i++) {
            int minIndex = i;
            for (int j = i+1; j < array.size(); j++) {
                if (array.get(j) < array.get(minIndex)) {
                    minIndex = j;
                }
                this.comps++;
            }
            if (i != minIndex) {
                swap(array, i, minIndex);
                this.swaps++;
            }
        }
        printCost(debug, this.swaps, this.comps);
        printSortedArray(array);
    }

}
