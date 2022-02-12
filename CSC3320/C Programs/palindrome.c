//Including the string and standard package
#include <stdio.h>
#include <string.h>
//Initial declaration of the palindrome function
int palin(char *message);
//Start of main method
int main(){
	//Character array to hold the input message
        char mess[200];
	//Prompting the user to enter the message
        printf("Enter the message:\n");
	//Reading the user input
        gets(mess);
	//Checking if the message is a palindrome and returning the appropriate message
        if(palin(&mess)){
		//If it is a palindrome, the function would return 1 and the below line would be printed to the terminal
                printf("This is a palindrome.\n");
        }else{
		//The below message would be printed if the message is not a palindrome and if the function returns 0
                printf("This is not a palindrome.\n");
        }
	//End of main method
        return 0;
}
//Definition of palin function with a pointer as a parameter
int palin(char *message){
	//A char pointer to iterate through the message
        char *p;
	/*An inital value to keep track of the index we are checking.
	It starts at -1 because it would be incremented after every iteration of the for loop*/
        int i = -1;
	//This finds the length of the message to consider border cases of 1 characters or null strings
        int len = strlen(message);
	//Checking the length of the message in cases where it would be a palindrome by default
        if(len == 1 || len == 0){
		//This returns true if it is a palindrome
                return 1;
        }else{
		//Initializing the for loop to loop through pointer addresses of the elements of the message array  
                for(p = &message[0]; p <= &message[len-1]; p++){
			//Incrementing the index counter to avoid a negative index
                        i = i + 1;
			//Comparing the elements at the beginning and corresponding end positions to check if they are different anywhere
			//I am converting it to lowercase to ensure that proper nouns are correctly judged
                        if(tolower(*p) != tolower(*(&message[len-1]-i))){
				//In the event that characters are different, a 0 is returned, stating that the message is not a palindrome
                                return 0;
                        }
                }
		//It is a palindrome, this returns 1 because all the compared characters were identical
                return 1;
        }
//End of palin method
}