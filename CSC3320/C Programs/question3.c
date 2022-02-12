//Importing the standard libraries
#include <stdio.h>
#include <stdlib.h>
//Initial declaration of the sorting method
int sort_numeric(float *array, char input, int length);
//Start of main method
int main(){
	//Declaring a pointer to a float array variable
	float *arr;
	//Allocating space for 1 float variable in the array
	arr = (float *) malloc( 1 * sizeof(float) );
	//Initializing the first element to avoid a garbage value print
	arr[0] = 0;
	//Initializing the loop index and length of array
	int i = 0; 
	int len = 0;
	//Variables to keep track of users entering values and sorting preference
	char inp, sor;
	//Prompting the user to enter sorting preference
	printf("Enter 'a' or 'A' for Ascending sort or 'd' or 'D' for Descending sort:\n");
	scanf("%s", &sor);
	//Declaring the variable to ensure that the user atleast enters 1 variable
	inp = 'y';
	//As long as the response is yes, the user can input values
	while(inp == 'y' || inp == 'Y'){
		//Prompting the user to enter value
		printf("Enter the element in this array\n");
		//Storing user value at the specific array index
		scanf("%f", &arr[i]);
		//Increment the count of the index by 1
		i = i + 1;
		//Asking the user if they would like to enter more values
		printf("Do you want to enter more elements?\n");
		//Storing response in variable inp
		scanf("%s", &inp);
		//If the user wishes to enter more values, the size of the array is increased by i+1 float variables
		if(inp == 'y' || inp == 'Y'){
			arr = realloc(arr, (i+1)*sizeof(float));
		}
	}
	//Declaring the length of the array
	len += i;
	//Calling the sorting method
	sort_numeric(arr, sor, len);
	//Unused space is freed
	free(arr);
	return 0;
//End of main method
}
//Definition of the sorting method
int sort_numeric(float *array, char input, int length){
	//Variables to store indecies for printing the sorted araay and performing the bubble sort operation
        int first, second, i;
	//Checking if the user wants to sort in ascending order
        if(input == 'a' || input == 'A'){
		//Implementing bubble sort by using pointer
                //Accessing the array's elements by using index
                for(first = 0; first < length; first++){
                        for(second = first + 1; second < length; second++){
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
                for(first = 0; first < length; first++){
                        for(second = first+1; second < length; second++){
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
        }
	//Stopping execution if the user entered invalid choice
	else{
                printf("Invalid option entered.\n");
                return 0;
        }
	//Printing the sorted array
        printf("Array is [");
        for(i = 0; i < length; i++){
                if(i != length-1){
                        printf("%f, ", array[i]);
                }else{
                        printf("%f]\n", array[i]);
                }
        }
	//End of sorting method
        return 0;
}
