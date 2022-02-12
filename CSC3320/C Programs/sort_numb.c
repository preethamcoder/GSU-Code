//Including the standard input-output library
#include <stdio.h>
//Initial declaration of the sorting method, with the parameters being the length of the array, sorting order, and a pointer to the array
int sort_numeric(float *array, char input, int len);
//Declaration of the main method
int main(){
	//Variable to hold the preferred sorting order of the user
	char inp;
	//Variables to hold the length and loop index
	int length, i; 
	//Prompting the user to enter preferred order of sorting
	printf("Enter 'a' or 'A' for ascending or 'd' or 'D' for descending\n");
	//Storing user input in variable inp
	scanf("%c", &inp);
	//Prompting the user to enter the length of the array
	printf("Enter the number of elements in the array:\n");
	//Storing the length of the array in variable len
	scanf("%d", &length);
	//Initializing the array with the number of elements in length
	float arr[length];
	//Prompting user to enter the elements in the array
	printf("Enter the elements\n");
	//Storing user inputs at ordered places in the array
	for(i = 0; i < length; i++){
		scanf("%f", &arr[i]);
	}
	//Calling the method to sort the array using bubble sort
	sort_numeric(&arr, inp, length);
	//End of main method
	return 0;
}
//Definition of the sorting method
int sort_numeric(float *array, char input, int len){
	//Variables to store indecies for printing the sorted araay and performing the bubble sort operation
	int i, first, second;
	//Checking if the user wants to sort in ascending order
	if(input == 'a' || input == 'A'){
		//Implementing bubble sort by using pointer
		//Accessing the array's elements by using index
		for(first = 0; first < len; first++){
			for(second = first + 1; second < len; second++){
				//Comparing the values of elements at given addresses and swapping them if the first is greater than the second
				if(*(array+first) >= *(array+second)){
					//A temp variable to hold the element at the first address
					double te;
					//Assigning the value at the first address to te
					te = *(array+first);
					//Assigning the value at the second address to the first address 
					*(array+first) = *(array+second);
					//Completing the swap by assigning the value of te to the second address
					*(array+second) = te;
				}
			}
		}
	//Checking if the user wants to sort in descending order
	}else if(input == 'd' || input == 'D'){
		//Implementing bubble sort by using pointer
		//Accessing the array's elements by using index
		for(first = 0; first < len; first++){
			for(second = first+1; second < len; second++){
				//Comparing the values of elements at given addresses and swapping them if the first is greater than the second
				if(*(array+first) <= *(array+second)){
					//A temp variable to hold the element at the first address
					double te;
					//Assigning the value at the first address to te
					te = *(array+first);
					//Assigning the value at the second address to the first address
					*(array+first) = *(array+second);
					//Completing the swap by assigning the value of te to the second address
					*(array+second) = te;
				}
			}
		}
	//Stopping execution if the user entered invalid choice
	}else{
		printf("Invalid option entered.\n");
		return 0;
	}
	//Printing the sorted array
	printf("Sorted Array is: [");
	for(i = 0; i < len; i++){
		if(i != len -1){
			printf("%f, ", array[i]);
		}else{
			printf("%f]\n", array[i]);
		}
	}
	//End of sorting method
	return 0;	
}
