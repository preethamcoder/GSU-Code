#include <stdio.h>
#include <string.h>
//Initial declaration of the function
int swap(char *mes1, char *mes2);
int main(){
	//A character array to store the first message
        char sen1[200];
	//Another character array to store the second message
        char sen2[200];
	//Prompting the user to enter the first message
        printf("Enter sentence 1\n");
	//Reading the first message from the user
        gets(sen1);
	//Prompting the user to enter the second message 
        printf("Enter sentence 2\n");
	//Reading the second message from the user
        gets(sen2);
	//Calling the method to swap the strings
        swap(&sen1, &sen2);
	//End of main method
        return 0;
}
//Defining the swap method with 2 pointers
int swap(char *mes1, char *mes2){
	//Finding length of message 1
        int len1 = strlen(mes1);
	//Finding length of message 2
        int len2 = strlen(mes2);
	//Displaying both strings first
        printf("Inital string values of 1 and 2: %s \t %s\n", mes1, mes2);
        //Ensuring that the lengths of both strings are the same by comparing the lengths - as per the last in the document instructions
	if(len1 != len2){
                printf("The messages are not of equal length.\n");
                return 0;
        }
	//Concatenating message 1 and 2 to make one giant message
        strcat(mes1, mes2);
	//Copying the the original message 1 from the large string to the second string
        strncpy(mes2, mes1, len2);
	//Printing both strings after swapping
	//Adding the length of one string to the first helps to extract the second message from the first 
        printf("Final values of strings 1 and 2: %s \t %s\n", mes1+len2, mes2);
        //End of function
	return 0;
}