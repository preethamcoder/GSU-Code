/**
 * 
 */
package csc1302;
import java.util.*;
/**
 * @author sthelluri1
 *
 */
public class ClientSorting2 {
	public static void SelectionSorter(String[] arrr) {
		//System.out.println("As there was no specification, I decided to sort this in ASCENDING ORDER.");
		System.out.println("This is selection sort:");
		System.out.println("The original array is " + Arrays.toString(arrr));
		for(int i = 0; i < arrr.length-1; i++) {
			int maxind = i;
			String temp;
			for(int j = i + 1; j < arrr.length; j++) {
				if(arrr[j].compareTo(arrr[maxind]) < 0) {
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
	public static void InsertSorter(String[] arrr) {
		//System.out.println("As there was no specification, I decided to sort this in ASCENDING ORDER.");
		System.out.println("This is insertion sort: ");
		System.out.println("The original array is " + Arrays.toString(arrr));
		String temp;
		int a = 1, b;
		while(a < arrr.length) {
			temp = arrr[a];
			b = a - 1;
			while(b >= 0 && arrr[b].compareTo(temp) > 0) {
				arrr[b+1] = arrr[b];
				b -= 1;
			}
			arrr[b+1] = temp;
			a += 1;
		}
		System.out.println("Sorted array is " + Arrays.toString(arrr));
		System.out.println();
	}
	public static void dualSort(int[] arrr) {
		System.out.println("This is the dual sort: ");
		System.out.println("The original array is " + Arrays.toString(arrr));
		int n = arrr.length;
		for(int i = 0, j = n-1; i < j; i++, j--) {
			int min = arrr[i], max = arrr[i];
			int min_ind = i, max_ind = i;
			for(int k = i+1; k <= j; k++) {
				if(arrr[k] > max) {
					max = arrr[k];
					max_ind = k;
				}else if(arrr[k] < min) {
					min = arrr[k];
					min_ind = k;
				}
			}
			swap(arrr, i, min_ind);
			
			if(arrr[min_ind] == max) {
				swap(arrr, j, min_ind);
			}else {
				swap(arrr, j, max_ind);
			}
		}
		System.out.println("Sorted array is " + Arrays.toString(arrr));
		System.out.println();
	}
	public static int[] swap(int[] arrr, int i, int j) {
		int temp = arrr[i];
		arrr[i] = arrr[j];
		arrr[j] = temp;
		return arrr;
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String[] array = new String[10];
		String[] array1 = new String[10];
		int[] array2 = new int[10];
		System.out.println("Enter the array that has to be sorted for the selection sort: ");
		for(int i = 0; i < array.length; i++) {
			array[i] = sc.nextLine();
		}
		SelectionSorter(array);
		System.out.println("Enter the array that has to be sorted for the insertion sort: ");
		for(int i = 0; i < array1.length; i++) {
			array1[i] = sc.nextLine();
		}
		InsertSorter(array1);
		System.out.println("Enter the array that has to be sorted for the dual sort: ");
		for(int i = 0; i < array1.length; i++) {
			array2[i] = sc.nextInt();
		}
		dualSort(array2);
	}

}
