//Including the standard input-output and string libraries
#include <stdio.h>
#include <string.h>
//Initially declaring the scorebylength function with a character pointer variable as a parameter
void scorebylength(char *input);
//Start of main method
int main(){
	//This is a variable to store the inital password entered by the user 
        char inpass[100];
	//Prompting the user to enter his password
        printf("Enter the password\n");
	//Reading the user input and storing it in the variable
        scanf("%s", &inpass);
	//Calling the method to check the safety of the password
        scorebylength(&inpass);
	//End of main method
        return 0;
}
//Definition of the scorebylength method
void scorebylength(char *input){
	//Calculating the length of the user input
        int len = strlen(input);
	//Calculating the deducted score based on the length by using the formula
        //5 points were taken off for every character short of 10 characters
	int decremented_score = 5*(10-len);
	//Checking the the deduction is greater than 30 and displaying appropriate messages
        if(decremented_score > 30){
		//Displaying the deduction and the message that the passowrd is unsafe and has to be reset
                printf("The deduction is %d points. The password is unsafe! Please reset.\n", decremented_score);
        }else{
		//Resetting the deduction to 0 incase the password is longer than 10 digits, as it would lead to the deduction of a negative score
                if(decremented_score < 0){
			//Resetting the deduction to 0 points
                        decremented_score = 0;
                }
		//Displaying the message that the password is safe along with the deducted score
                printf("The deduction is %d points. The password is safe.\n", decremented_score);
        }
	//End of scorebylength method
}