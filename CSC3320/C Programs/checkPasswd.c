//Including the standard input-output and string libraries
#include <stdio.h>
#include <string.h>
//Initial declaration of the scorebylength function
void scorebylength(char *input);
//Start of main method
int main(){
	//Variable to hold the value of the user-entered password
        char inpass[100];
	//Prompting the user to enter the password
        printf("Enter the password\n");
	//Storing the input in the inpass variable
        scanf("%s", &inpass);
	//Checking the safety of the password with this method call
        scorebylength(&inpass);
        return 0;
//End of the main method
}
//Definition of the scorebylength method with a char pointer as a parameter
void scorebylength(char *input){
	//Initial variables to keep track of the indexes of for loops 
        int i, j = 0;
	//Calculating the length of the user-entered password
        int len = strlen(input);
	//Initializing the deduction score variable and setting it to 0
        int decremented_score = 0;
	//Initializing the variable to make sure upper case letters are in the password
        int cap_strike = 0;
        //Initializing the variable to make sure numbers/digits are in the password
	int num_strike = 0;
	//Initializing the variable to make sure lower case letters are in the password
        int low_strike = 0;
	//Initializing the variable to make sure not more than 2 concecutive letters/numbers are present in any place
        int comb_strike = 0;
	//Iterating through every character in the password to check for upper case, lower case letters, and numbers
        for(i = 0; i < len; i++){
		//Checking if the current character is either lower case or a digit - a.k.a not upper case
                if((input[i]>='a' && input[i]<='z')||(isdigit(input[i]))){
                        //Adding 1 non-upper case score to the strikes counter
			cap_strike = cap_strike + 1;
                }
                //Checking if the current character is not a digit
		if(!(isdigit(input[i]))){
                        //Adding 1 non-digit score to the strikes counter
			num_strike = num_strike + 1;
                }
		//Checking if the current character is either upper case or a digit - a.k.a not lower case
                if((input[i]>='A' && input[i]<='Z')||(isdigit(input[i]))){
                        //Adding 1 non-lower case score to the strikes counter
			low_strike = low_strike + 1;
                }
        }
	//Initializing a counter to 3 indices short of the total length, as I am comparing 3 characters at once
        while(j <= len-3){
		Checking if the first character and the second are concecutive and later if the first character and third character in this set are separated by 2 ASCII values
                if(((int)input[j])+1 == (int)input[j+1] && ((int)input[j])+2 == (int)input[j+2]){
                        //Adding 1 concecutive combination score to the strikes counter
			comb_strike = comb_strike + 1;
                }
		//Incrementing the jth indec to reach the next set of 3 characters
                j++;
        }
	//Checking if there is atleast 1 occerence where more than 2 concecutive characters are present together
        if(comb_strike > 0){
		//Adding 20 points to the deducted score
                decremented_score = decremented_score + 20;
        }
	//Checking if there are no upper case letters, as the prior if condition would be true len(n) times
        if(cap_strike == len){
		//Adding 20 points to the deducted score
                decremented_score = decremented_score + 20;
        }
	//Checking if there are no numbers, as the prior if condition would be true len(n) times
        if(num_strike == len){
                //Adding 20 points to the deducted score
		decremented_score = decremented_score + 20;
        }
	//Checking if there are no lower case letters, as the prior if condition would be true len(n) times
        if(low_strike == len){
		//Adding 20 points to the deducted score
                decremented_score = decremented_score + 20;
        }
        //Checking if the deducted score is more than 30 points
	if(decremented_score > 30){
		//In the event of the deduction score exceeding 30 points, the user is told that the password is unsafe and has to be reset
                printf("The deduction is %d points. The password is unsafe! Please reset.\n", decremented_score);
        }else{
		//Printing to the terminal that the password is safe along with the deduction score, in the event that the deducted score is less than 30
                printf("The deduction is %d points. The password is safe.\n", decremented_score);
        }
//End of scorebylength method
}