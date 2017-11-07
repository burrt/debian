package sorts;

import java.util.List;

public class Sort {

    public static void swap(List<Integer> array, int i, int j) {
        int temp = array.get(j);
        array.set(j, array.get(i));
        array.set(i, temp);
    }

    public static void printSortedArray(List<Integer> array) {
        System.out.println("Sorted: " + array);
        System.out.println("--------------------------------------------------------------------------------------");
    }

    public static void printCost(Boolean debug, int swaps, int comps) {
        if (debug) {
            System.out.printf("Swaps: %d\n", swaps);
            System.out.printf("Comparisons: %d\n", comps);
        }
    }
}
