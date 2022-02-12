//Including the standard input-output library
#include <stdio.h>
//Defining a phone-code structure with 2 attributes 
struct dialing_code{
	//This hold the name of the country
        char *country;
	//This holds the dialing code of the country
        int code;
//I have defined a country-code dialier with 21 countries, as per the requirement which had a minimum of 20
}; const struct dialing_code country_code[] = {{"Argentina", 54}, {"Brazil", 55}, {"Bangladesh", 880}, {"China", 86}, {"Colombia", 57}, {"Egypt", 30}, {"France",33}, {"India", 91}, {"Indonesia", 62}, {"Italy", 39}, {"Japan", 81}, {"Mexico", 52}, {"Nigeria", 234}, {"Pakistan", 92}, {"Philippines", 63}, {"Poland", 48}, {"Russia", 7}, {"South Africa", 27}, {"South Korea", 82}, {"United Kingdom", 44}, {"United States", 1}};
//Initial declaration of the lookup function
int ind_ext(int *code1);
//The beginning of the main method
int main(){
	//A variable to hold the user input of country code
        int con_code;
	//Prompting the user to enter the country code
        printf("Enter the code of the country's phone numbers.\n");
        //Storing the country code in a variable
	scanf("%d", &con_code);
	//Since this is a function with an integer return type, I put it inside an if statement
	//As long as the country is in the list, the user will receive an output with a country's name 
        if(ind_ext(&con_code)){
		//This returns the country name at the index returned by the function
		//I added the -1 after the function call because I have added 1 to the return value in the event of a successful find inside the function
                printf("The country is %s.\n", country_code[ind_ext(&con_code)-1].country);
        }else{
		//This would display in the event of an unsuccessful find in the function
                printf("The country was not found in this directory!\n");
        }
	//End of main method
        return 0;
}
//Definition of the ind_ext method with an integer pointer as a parameter
int ind_ext(int *code1){
	//A variable to keep track of the index of the for loop
        int i;
	//Assigning the value of the pointer to another integer variable to avoid conflicts while comparing accross types
        int comp = *code1;
	//Starting a for loop to loop through all the contents in the directory
        for(i = 0; i < 21; i++){
		//Checking if the country code corresponds to the code at any particular index in the phonebook
                if(country_code[i].code == comp){
			//In case of a successful match, the position of the "code," (index+1) is returned
                        return(i+1);
                }
        }
	//This would return 0 in case of a failuer, as the country is not in the directory
        return 0;
//End of the ind_ext method
}