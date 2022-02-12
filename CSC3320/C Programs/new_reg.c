//Including the standard libraries
#include <stdio.h>
#include <string.h>
#include <time.h>
//Defining structure to hold information
struct user {
    char fname[200];
    char lname[200];
    int dd,mm,yy;
    char sex[200];
    int pdd,pmm,pyy;
    int dnumber;
    char vaccinetype[200];
    char zip[200];
};
//Declaring the methods before defining them in detail
int getage(int pdate, int pmonth, int pyear, int bdate, int bmonth, int byear);
void gen_code(struct user var);
void display(struct user var, int i);
//Start of main method
int main(void){
    //Variable to hold the number of users to be registered 
    int reg;
    //Prompting the user to enter the number of people who have to be registered
    printf("Enter the number of people you want to register:\n");
    //Storing the user input in reg
    scanf("%d", &reg);
    //Calling the regis function to register the users
    regis(reg);
    //Exiting main method
    return 0;
//End of main method
}
//Function to find age given two dates; it takes the present date, month, and year, and the birth date, month, and year as parameters
int getage(int pdate, int pmonth, int pyear, int bdate, int bmonth, int byear) {
     //An array containing the number of days in a month based on index (eg: January, February, March...)
     int month[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
     //Checking if the day of birth is greater than the current day 
     if (bdate > pdate) {
	    //Adding the days to the current date
            pdate = pdate + month[bmonth - 1];
	    //Decrementing the current month by 1, as the days have been added to account for the excess days before the next month
            pmonth = pmonth - 1;
     }
     //Checking if the month of birth is greater than the serial number of the current month
     if (bmonth > pmonth) {
	    //Decrementing the current year by 1, as person is not a whole year older
            pyear = pyear - 1;
	    //Adding a whole year to the current month, so that it can accurately make up for the difference between the next year
            pmonth = pmonth + 12;
     }
     //The below 2 computations are useless in this situation, but I did that to compute the exact age in months and days
     //int final_date = pdate - bdate;
     //int final_month = pmonth - bmonth;
     //Computing the final age in years
     int final_year = pyear - byear;
     //Returning the age of the person as an integer
     return final_year;
//End of method for age calculation
}
//Method to facilitate registration of users
void regis(int len){
    //Variable to store the choice of the user
    int choice;
    //Variable to store the unique id generated for each user
    char id[9];
    //Character variable to store age of the user
    char age[3];
    //This variable is a substitute for length
    int tot;
    //Assigning the value of len to tot
    tot = len;
    //Declaring an aray of structures of length tot
    struct user u1[tot];
    //Variable to hold the index of the loop
    int i;
    for(i = 0;i<tot;i++){
	//Prompting the user to enter the details
        printf("Enter details for Person %d:\n",i+1);
        //Prompting the user to enter first name
        printf("Enter First Name: ");
        scanf("%s", u1[i].fname);
        //Prompting the user to enter last name
        printf("Enter Last Name: ");
        scanf("%s", u1[i].lname);
        //Prompting the user to enter birthdate
        printf("Enter Birth Date(mm/dd/yyyy): ");
        scanf("%d/%d/%d",&u1[i].mm,&u1[i].dd,&u1[i].yy);
        //Prompting the user to choose sex
        printf("Choose sex: \n");
        printf("\t1. Male\n");
        printf("\t2. Female\n\t3. Do not wish to identify\n\tEnter choice: ");
        scanf("%d", &choice);
        //Checking if the choice is valid
        if(choice == 1){
            strcpy(u1[i].sex, "Male");
        }else if(choice == 2){
            strcpy(u1[i].sex, "Female");
        }else if(choice == 3){
            strcpy(u1[i].sex, "Do not wish to identify");
        }else{
                printf("Invalid choice for gender!\n");
                return 1;
        }
        //Prompting the user to enter dose number
        printf("Enter Dose Number: ");
        scanf("%d", &u1[i].dnumber);
	//Checking if the dose number is valid
        if(!(u1[i].dnumber == 1 || u1[i].dnumber == 2)){
            printf("Please enter valid dose number.\n");
            //return 1;
        }
        //Prompting the user for previous dose date if it is the second dose
        if(u1[i].dnumber == 2){
            printf("Enter Previous Dose Date(mm/dd/yyyy): ");
            scanf("%d/%d/%d",&u1[i].pmm,&u1[i].pdd,&u1[i].pyy);
        }
        //Prompting the user to choose the desired vaccine
        printf("Choose type of vaccine : \n");
        printf("\t1. Pfizer\n");
        printf("\t2. Moderna\n");
        printf("\t3. Johnson&Johnson\n\tEnter choice: ");
        scanf("%d", &choice);
        //Check that choosen vaccine type is valid
        if(choice == 1){
            strcpy(u1[i].vaccinetype, "Pfizer");
        }else if(choice == 2){
            strcpy(u1[i].vaccinetype, "Moderna");
        }else if(choice == 3){
            strcpy(u1[i].vaccinetype, "Johnson&Johnson");
        }else{
            printf("Please choose valid type of vaccine.\n");
            //return 1;
        }
        //Prompting the user to enter the zip code
        printf("Enter Zip: ");
        scanf("%s", &u1[i].zip);
        }
	//Printing all the information about the registered users
	printf("Information about registered people:\n");
	for(i = 0; i < tot; i++){
	    //Calling the display method with the gen_code method inside it
	    display(u1[i], i);
        }
//End of registration method
}
//Method to generate a unique code for every user
void gen_code(struct user var){
	//Variable to hold the unique id
        char id[9];
        //Copy first letter of first and last name
        id[0] = var.fname[0];
        id[1] = var.lname[0];
        //Get current date in the local time-zome
        time_t t = time(NULL);
        struct tm tm = *localtime(&t);
        //Calculate age of user by calling getage() function
        int ageTemp = getage( tm.tm_mday,tm.tm_mon + 1,tm.tm_year + 1900,var.dd,var.mm,var.yy);
        //Copy the age into different indices of the id
        id[2] = (char)(ageTemp/10+ '0');
        id[3] = (char)(ageTemp%10+ '0');
        //Copy first letter of preferred vaccine type
        id[4] = var.vaccinetype[0];
        //Copy last 3 digit of the zip code
        id[5] = var.zip[2];
        id[6] = var.zip[3];
        id[7] = var.zip[4];
	//Assign null to last cahracter space to avoid garbage value print
        id[8] = '\0';
	//Printing final value of the unique id
        printf("Unique code: %s\n\n", id);
}
//Method to display the details of the user
void display(struct user var, int i){
	//Printing registration number, first name, last name, birthday, sec, dose number, previous date (if applicable), zip code, and the unique code for the user 
        printf("\nPerson %d:\n", i+1);
        printf("\nFirst Name : %s\n",var.fname);
        printf("Last Name : %s\n",var.lname);
        printf("Birthdate : %d/%d/%d\n",var.mm,var.dd,var.yy);
        printf("Sex : %s\n",var.sex);
        printf("Dose Number : %d\n",var.dnumber);
        if(var.dnumber == 2){
            printf("Previous Dose Date : %d/%d/%d\n",var.pmm,var.pdd,var.pyy);
        }
        printf("Vaccine type : %s\n",var.vaccinetype);
        printf("Zip : %s\n",var.zip);
	//Calling the gen_code method to get the unique code for each user
        gen_code(var);
//End of display method
}
