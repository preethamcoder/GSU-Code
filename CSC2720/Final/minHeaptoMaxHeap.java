import java.util.*; //Importing all packages from java.util
class minHeaptoMaxHeap { //Class to convert Minimum Heap to Maximum Heap
	static void toMax(int arr[], int i, int size) { //Method to heapify the subtree where the root and size have been passed
		int right = 2 * i + 2; //The right node variable
		int left = 2 * i + 1; //The left node variable
		int largest = i; //Variable to store the larger value of those two variables

		if (left < size && arr[left] > arr[i]) { //Checking if the left sub node is less than size and if it is greater than current element
			largest = left; //Saves the integer to a variable
		}
		if (right < size && arr[right] > arr[largest]) { //Check if the right sub node is less than size and if it is greater than current element
			largest = right; //Saves the integer to a variable
		}
		if (largest != i) { //If largest value was not the same as the passed value, swap those values
			int temp = arr[i]; //Saves the current element to a temp variable
			arr[i] = arr[largest]; //Assigning value of the largest index to the current 
			arr[largest] = temp; //Finishing the swap by assigning temp to the copied value
			toMax(arr, largest, size); //Recursive method to go further into the heap
		}
	}
	static void convert(int arr[], int size) { //Method to convert minimum heap to maximum heap 
		if (size < 1) { //Checks if the size is less than 1
			System.out.println("Empty Array"); //Prints "Empty Array" and exits the method if the condition is true 
		} else { //Execution of the second branch if it is not empty
			int i = (size - 2) / 2; //Variable with value to start from the one side of the heap
			while (i >= 0) { //While loop to compare value with variable i and go further into the heap
				toMax(arr, i, size); //Calling the function to heapify the subtree
				i--; //Decrements the value of i
			}
		}
	}
	public static void main(String[] args) { //Start of main Method
		int arr[] = { 3, 5, 9, 6, 8, 20, 10, 12, 18, 9 }; //Initializing the array
		System.out.print("Min Heap array: "); //Printing the label for the original array
		System.out.println(Arrays.toString(arr)); //Printing the orginal array by converting the array to string
		convert(arr, arr.length); //Calls the method to convert the minimum heap to maximum heap
		System.out.print("Max Heap array: "); //Printing the label converted array 
		System.out.println(Arrays.toString(arr)); //Printing the converted array by converting the array to string
        //End of main method
	}
}
//Time Complexity: O(n)
//Space Complexity: O(n)
