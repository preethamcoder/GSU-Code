package csc1302;
import java.util.*;

public class Search {
	public static int sequentialSearch(int[] array1, int x) {
		for(int i = 0; i < array1.length; i++) {
			if(x == array1[i]) {
				return i;
			}
		}
		return -1;
	}
	public static int binarySearch(int[] arya, int elem) {
		int low = 0;
		int high = arya.length - 1;
		int key;
		if(elem < arya[low] || elem > arya[high]){
			return -1;
		}
		while(low <= high){
			key = (low + high)/2;
			if(elem < arya[key]){
				high = key - 1;
			}else if(elem > arya[key]){
				low = key + 1;
			}else{
				return key;
			}
		}
		return -1;
	}
	public static int binarySearchRecur(int[] ar, int ele, int strind, int endin) {
		int key = (strind + endin-1)/2;
		if(ele < ar[strind] || ele > ar[endin-1]) {
			return -1;
		}
		if(ar[key] == ele) {
			return(key);
		}else if(ar[key] > ele) {
			return binarySearchRecur(ar, ele, strind, key - 1);
		}else {
			return binarySearchRecur(ar, ele, key + 1, endin);
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] array = new int[10];
		int[] arr2 = new int[10];
		int[] arr3 = new int[10];
		int element, start_ind, end_ind;
		int index, ind1, ind2;
		Scanner sc = new Scanner(System.in);
		System.out.println("You need to enter an array of 10 numbers, enter them one after the other.");
		for(int d = 0; d < 10; d++) {
			array[d] = sc.nextInt();
		}
		System.out.println("What is the element you are looking for? ");
		element = sc.nextInt();
		System.out.println("Original array is: ");
		for(int d = 0; d < 10; d++) {
			System.out.println(array[d]);
		}
		index = sequentialSearch(array, element);
		System.out.println("The index of " + element + " is " + index);
		System.out.println("Time for a binary search, enter elements of the array in ascending order: ");
		for(int i = 0; i < 10; i++) {
			arr2[i] = sc.nextInt();
		}
		System.out.println("Enter the element you want to search:");
		element = sc.nextInt();
		System.out.println("Original array is: ");
		for(int d = 0; d < 10; d++) {
			System.out.println(arr2[d]);
		}
		ind1 = binarySearch(arr2, element);
		System.out.println("The index of " + element + " is " + ind1);
		System.out.println("This is to test binarysearch with recursion, enter 10 elemetns for the sorted array one-by-one.");
		for(int i = 0; i < 10; i++) {
			arr3[i] = sc.nextInt();
		}
		System.out.println("Enter the element you want to search:");
		element = sc.nextInt();
		System.out.println("Enter the start index of the array:");
		start_ind = sc.nextInt();
		System.out.println("Enter the end index of the array:");
		end_ind = sc.nextInt();
		System.out.println("Original array is: ");
		for(int d = 0; d < 10; d++) {
			System.out.println(arr3[d]);
		}
		ind2 = binarySearchRecur(arr3, element, start_ind, end_ind);
		System.out.println("The index of " + element + " is " + ind2);
	}
}
