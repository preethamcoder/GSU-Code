/*The purpose of this program is to check whether an array is sorted or not.
 * Author: Preetham Thelluri
 * Course: CSC 1302 (Principles of Computer Science II)
 * CRN: 84816
 */
package csc1302;
import java.util.*;
import java.util.Scanner;

public class ArraySorter {
	public static boolean isSorted(int[] array) {
		if(array.length == 1) {
			return(true);
		}
		for(int x = 1; x < array.length; x++) {
			if(array[x-1] > array[x]) {
				return(false);
			}
		}
		return(true);
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number of elements in your array: ");
		int a = sc.nextInt();
		int[] arry = new int[a];
		System.out.println("Now, please enter the elements of your array one after the other.");
		//Like said in the prompt, I am assuming that every array has at least 1 element.
		for(int i = 0; i < a; i++) {
			arry[i] = sc.nextInt();
		}
		System.out.println(isSorted(arry));
	}
	
}
