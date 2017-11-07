package sorts;

import java.util.ArrayList;
import java.util.List;

public class BubbleSort extends Sort{
    private int swaps = 0;
    private int comps = 0;

    public void sort(List<Integer> a, Boolean debug) {
        System.out.println("Bubble sort");
        List<Integer> array = new ArrayList<Integer>(a);

        for (int i = 0; i < array.size(); i++) {
            int innerSwaps = 0;
            for (int j = 0; j < array.size()-1; j++) {
                if (array.get(j+1) < array.get(j)) {
                    swap(array, j, j+1);
                    this.swaps++;
                    innerSwaps++;
                }
                this.comps++;
            }
            if (innerSwaps == 0) {
                break;
            }
        }
        printCost(debug, this.swaps, this.comps);
        printSortedArray(array);
    }

}
