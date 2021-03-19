/*
 * @author Preetham Thelluri
 * The purpose of this lab is to reverse, return the maximum, and double the elements of the reversed array. 
 * This considers arrays with 10 elements.
 */
package csc1302;
import java.util.*;
public class Lab2{

	public static void reverse(int[] arr1) {
		for(int m = 0; m < arr1.length/2; m++) {
			int temp = arr1[m];
			arr1[m] = arr1[arr1.length - m -1];
			arr1[arr1.length - m - 1] = temp; 
		}
		System.out.println("Array in reversed order: " + Arrays.toString(arr1).replace("[", "").replace("]", ""));
	}
	public static void computeTwice(int[] arr1) {
		//reverse(arr1);
		for(int k = 0; k < arr1.length; k++) {
			arr1[k] *= 2;
		}
		System.out.println("Array with twice the values: " + Arrays.toString(arr1));
	}
	public static void getmax(int[] arr1) {
		int maxi = arr1[0];
		if(arr1.length == 1) {
			System.out.println("Maximum element = " + arr1[0]);
		}else{
			for(int z = 1; z < arr1.length; z ++) {
				if(arr1[z] > maxi) {
					maxi = arr1[z];
				}
			}
			System.out.println("Maximum element = " + maxi);
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int x = 10;
		//System.out.println("Enter the number of elements in your array: ");
		//x = sc.nextInt();
		int[] arr = new int[x]; 
		System.out.println("Time to enter the elements of your array.");
		for(int i = 0; i < x; i++) {
			System.out.println("Enter a number: ");
			arr[i] = sc.nextInt();
		}
		reverse(arr);
		getmax(arr);
		computeTwice(arr);
	}

}
