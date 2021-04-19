//Including the standard input-output and string library
#include <stdio.h>
#include <string.h>
//Initial declaration of the sort method
void sort_alphabetic(char *sets[], int i, int j);
//Start of the main method
int main(void) {
    //Defining a pointer to the test array
    char *words[] = {"Systems", "Programming", "Deep", "Learning", "Internet", "Things", "Robotics", "Course"};
    //Declaring both int variables to hold indecies of the array and later print them
    int ind, ind2;
    /*//Converting it to lower case
    for(ind = 0; words[ind]; ind++){
        strcpy(words[ind], strlwr(words[ind]));
    }*/
    //Calling the sorting method
    sort_alphabetic(&words, ind, ind2);
    //End of main method
    return 0;
}
//Definition of the sorting method
void sort_alphabetic(char *sets[], int i, int j){
    //A character pointer to temporarily store the word at an address
    char *tmp;
    //Character to store the sort order preference
    char inp;
    //A variable to hold the length of the array while printing at the end
    int count;
    //Prompting the user to enter the sorting preference
    printf("Enter 'a' or 'A' for ascending order or 'd' or 'D' for descending order:\n");
    //Storing the user input in the inp variable
    scanf("%s", &inp);
    //Starting the for loop to implement the bubble sort algorithm
    //Outer loop containing the a pointer to the first word
    for (i = 0; sets[i]; i++){
        //Inner loop containing a pointer to the first and then subsequent words
        for (j = 0; sets[j]; j++){
	    //Checking if the user wants to sort in ascending order
            if (inp == 'a' || inp == 'A'){
		//Comparing the elements, if one comes before the other 
		if (strcmp(sets[i], sets[j]) < 0){
		    //Swapping the elements at the addresses
                    tmp = sets[i];
                    sets[i] = sets[j];
                    sets[j] = tmp;
                }
            }
            //Checking if the user wants to sort in descending order
	    else if (inp == 'd' || inp == 'D'){
		//Comparing the elements, if one come after the other
                if (strcmp(sets[i], sets[j]) > 0){
		    //Swapping elements at addresses
                    tmp = sets[i];
                    sets[i] = sets[j];
                    sets[j] = tmp;
                }
            }
        }
    }
    //Calculating the number of elements in the array
    for(i = 0; sets[i]; i++){
	count = count + 1;
    }
    //Checking if the sorting preference is ascending and using a different index to print the array to avoid the null character at the first
    if(inp == 'a' || inp == 'A'){
        printf("Post sorting array:\n");
	//Printing the elements of the array one after the other
        for(i = 1; sets[i]; i++){
            printf("%s\n", sets[i]);
        }
    }
    //Checking if the choice is descending
    else if(inp =='d' || inp == 'D'){
	//Printing the elements in the 2-D character array, one after the other
        printf("Post sorting array:\n");
	for(i = 0; i < count; i++){
            printf("%s\n", sets[i]);
        }
    }else{
	//Printing error message if the user entered an invalid sort preference
	printf("Invalid option entered for sorting\n");
    }
//End of sorting method
}
