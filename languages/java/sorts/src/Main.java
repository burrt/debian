import sorts.BubbleSort;
import sorts.InsertionSort;
import sorts.SelectionSort;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;


/* Some basic sorting algorithms - trying a different approach to printing the sorts.
 * This will automatically run all the sorts and compares the costs.
 *
 * Author: Geoff
 */
public class Main {
    private final static int arraySize = 15;


    public static void main(String[] args) {
        Random rand = new Random();

        BubbleSort bubbleSort  = new BubbleSort();
        InsertionSort insertSort = new InsertionSort();
        SelectionSort selectSort = new SelectionSort();

        // Generate a random array of numbers - they could be sorted!
        List<Integer> toSortArray = new ArrayList<Integer>();
        for (int i = 0; i < arraySize; i++) {
            toSortArray.add(rand.nextInt(100));
        }

        System.out.println("--------------------------------------------------------------------------------------");
        System.out.println("Unsorted: " + toSortArray);
        System.out.println("--------------------------------------------------------------------------------------");

        bubbleSort.sort(toSortArray, true);
        insertSort.sort(toSortArray, true);
        selectSort.sort(toSortArray, true);
    }
}
