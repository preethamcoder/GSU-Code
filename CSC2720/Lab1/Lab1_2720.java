// Lab 1 - 2720
// Author: Preetham Thelluri
/*
PART 1:
*********************************************************************************************************
int y = 15;
while(y>=0){
    System.out.println("y");
    y = y - 1;
}
This code will run 16 times, since the initial value is 15 and it will run till the value would be less than 0. That would be when y = -1, 15 -(-1) = 16 times.
*********************************************************************************************************
int y = 5;
do{
    System.out.println("y");
    y -= 1;
}while(y<0);
This code will run only 1 time. This is a do-while loop, and it will execute atleast 1 time. Since the value of y is greater than 0, it will break out of the loop after the first iteration.
*********************************************************************************************************
int y = 5;
while(y>0){
    System.out.println("y");
}
This code will run infinite number of times, as this is an infinite loop. The value of y is greater than 0 and is never altered, so this loop will keep running forever.
*********************************************************************************************************
for(i = 0; i<140; i++){
    System.out.println("y");
}
This code will run 140 times, as it's initial value is 0 and it runs till the value is 139 (integer less than 140). 139+1=140 times.
*********************************************************************************************************
int y = 3;
do{
    System.out.println("y");
    y += 2;
}while(y<=9);
This code will run 4 times, as there are 4 odd numbers between 3 and 9 inclusive. This code will run as long as the value is less than or equal to 9, and it will run on every odd number because it is incremented by 2, starting at 3.
*********************************************************************************************************
for(i = 50; i<540; i++){
    for(j = 2; j < 10; j++){
        System.out.println("y");
    }
}
This code will run 4720 times, as 590*8 = 4720. The inner for loop runs 8 times for every one time the outer loop runs. The inner loop starts at 2 and ends when the number is less than 10 (8 iterations). The outer loop starts at 50 and end when the number is less than 640 (590 iterations). It has a total of 590*8 = 4720 iterations. 
**********************************************************************************************************
*/
//PROBLEM 2:
import java.util.Scanner;
import java.util.ArrayList;
public class Lab1_2720{
    public static void arrayintersection(int[] arr1, int[] arr2){
        //HERE, I AM ASSUMING THEY HAVE UNIQUE ELEMENTS (AS SAID IN THE PROMPT)
        ArrayList<Integer>res = new ArrayList<Integer>();
        for(int i = 0; i < arr2.length; i++){
            for(int j = 0; j < arr1.length; j++){
                if(arr2[i] == arr1[j]){ //Checking if a chosen element of hte shorter array has a match
                    res.add(arr2[i]); //Adding the specific element to the ArrayList
                }
            }
        }
        System.out.println(res); //Printing the result out
    }
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int a, b;
        System.out.println("Enter the number of elements in your first array: ");
        a = sc.nextInt(); //Asking for the length of the first array
        int myarr1[] = new int[a]; //Initializing the first array
        System.out.println("Enter each element in the array, one after the other!"); //Populating the first array
        for(int i = 0; i < a; i++){
            myarr1[i] = sc.nextInt();
        }
        System.out.println("Enter the number of elements in your second array");
        b = sc.nextInt(); //Asking the number of elements in the second array
        int myarr2[] = new int[b]; //Initializing the second array
        System.out.println("Enter each element in the array, one after the other!"); //Populating the second array
        for(int i = 0; i < b; i++){
            myarr2[i] = sc.nextInt();
        }
        //Sending the array to the method with the longer array first
        if(a >= b){
            arrayintersection(myarr1, myarr2);
        }else{
            arrayintersection(myarr2, myarr1);
        }
    }
}
