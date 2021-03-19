import java.sql.Time;
import java.util.*;

public class matrix{
    public static void main(String[] args) {
        int dimensions; //This stores the dimensions of the square matrix
        String resp; //This is a variable to store whether a user wants to continue or not
        Random rand = new Random(); //I have created an object of the random class; this will help to populate matrices.
        Scanner sc = new Scanner(System.in); //This is a new scanner I created.
        do{
            final long startTime = System.currentTimeMillis(); //I took in the start time here
            System.out.println("Enter 50 as the dimension of the square matrix");
            dimensions = sc.nextInt();//Asking the user to enter a specific numer (50) as the dimension of the matrix.
            while(dimensions != 50){//Keep prompting the user till the desired number is entered.
                System.out.println("You did not enter 50. Enter 50 as the dimension of the square matrix: ");
                dimensions = sc.nextInt();
            }
            int matrix1[][] = new int[dimensions][dimensions];//Initializing both matrices, one after the other
            int matrix2[][] = new int[dimensions][dimensions];
            for(int i = 0; i < dimensions; i++){//Populating both the matrices, one after the other
                for(int j = 0; j < dimensions; j++){
                    matrix1[i][j] = rand.nextInt(50);
                    matrix2[i][j] = rand.nextInt(50);
                }
            }
            //Printing matrix 1 using an "Arrays" library function instead of a double nested for-loop
            System.out.println("Matrix 1 is as follows: ");
            System.out.println(Arrays.deepToString(matrix1));
            System.out.println();
            //Printing matrix 2 using an "Arrays" library function instead of a double nested for-loop
            System.out.println("Matrix 2 is as follows: ");
            System.out.println(Arrays.deepToString(matrix2));
            System.out.println();
            //Printing the resultant matrix after computing it
            System.out.println("The resultant matrix is as follows: ");
            int result[][] = new int[dimensions][dimensions]; //Initialized the resultant matrix
            //Computing the resulatant matrix using a triple for loop
            for(int i = 0; i < dimensions; i++){
                for(int j = 0; j < dimensions; j++){
                    for(int k = 0; k < dimensions; k++){
                        result[i][j] += matrix1[i][k]*matrix2[k][j];
                    }
                }
            }
            final long endTime = System.currentTimeMillis(); //Encapsulating the end time of the algorithm
            System.out.println();
            //Displaying the final matrix
            System.out.println(Arrays.deepToString(result));
            System.out.println();
            //Displaying the execution time
            System.out.println("Total execution time is....: "+ (endTime-startTime) + " milliseconds.");
            System.out.println();
            //Asking if the user wants another iteration
            System.out.println("Would you like to continue? (yes/no)");
            resp = sc.next();
        }while(resp.equals("yes") || resp.equals("Yes")); //Checking the condition and running the loop again!
        sc.close(); //Closing the Scanner if the user does not want to go again.
    }
}