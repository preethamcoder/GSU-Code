/**
 * 
 */
package csc1302;
import java.util.*;

/**
 * @author Preetham Thelluri
 *
 */
public class ClientSorting {

	/**
	 * @param args
	 */
	public static void InsertSorter(int[] arrr) {
		System.out.println("As there was no specification, I decided to sort this in ASCENDING ORDER.");
		System.out.println("This is insertion sort: ");
		System.out.println("The original array is " + Arrays.toString(arrr));
		int temp, b;
		int a = 1;
		while(a < arrr.length) {
			temp = arrr[a];
			b = a - 1;
			while(b >= 0 && arrr[b] > temp) {
				arrr[b+1] = arrr[b];
				b -= 1;
			}
			arrr[b+1] = temp;
			a += 1;
		}
		System.out.println("Sorted array is " + Arrays.toString(arrr));
		System.out.println();
	}
	public static void BubbleSorter(int[] arrr) {
		System.out.println("This is bubble sort: ");
		System.out.println("The original array is " + Arrays.toString(arrr));
		int temp;
		for(int a = 0; a < arrr.length-1; a++) {
			for(int b = 0; b < arrr.length-1; b++) {
				if(arrr[b] < arrr[b+1]) {
					temp = arrr[b];
					arrr[b] = arrr[b+1];
					arrr[b+1] = temp;
				}
			}
		}
		System.out.println("Sorted array is " + Arrays.toString(arrr));
		System.out.println();
	}
	public static void SelectionSorter(int[] arrr) {
		System.out.println("As there was no specification, I decided to sort this in ASCENDING ORDER.");
		System.out.println("This is selection sort:");
		System.out.println("The original array is " + Arrays.toString(arrr));
		for(int i = 0; i < arrr.length-1; i++) {
			int maxind = i;
			int temp;
			for(int j = i + 1; j < arrr.length; j++) {
				if(arrr[j] < arrr[maxind]) {
					maxind = j;
				}
			}
			temp = arrr[i];
			arrr[i] = arrr[maxind];
			arrr[maxind] = temp;
		}
		System.out.println("Sorted array is " + Arrays.toString(arrr));
		System.out.println();
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int[] ar1 = new int[10];
		int[] ar2 = new int[10];
		int[] ar3 = new int[10];
		System.out.println("Enter the elements for the selection sort array");
		for(int i = 0; i < ar1.length; i++) {
			ar1[i] = sc.nextInt();
		}
		SelectionSorter(ar1);
		System.out.println("Enter the elements for the bubble sort array");
		for(int i = 0; i < ar2.length; i++) {
			ar2[i] = sc.nextInt();
		}
		BubbleSorter(ar2);
		System.out.println("Enter the elements for the insertion sort array");
		for(int i = 0; i < ar3.length; i++) {
			ar3[i] = sc.nextInt();
		}
		InsertSorter(ar3);
	}

}
