import java.util.*;
class TimesAndInstructors
{
   public static void main(String[] args)
   {
       String courses[][] = new String[6][3];
       courses[0][0] = "Course";
       courses[0][1] = "Time";
       courses[0][2] = "Instructor";
       courses[1][0] = "CIS101";
       courses[1][1] = "Mon 9 am";
       courses[1][2] = "Farrell";
       courses[2][0] = "CIS210";
       courses[2][1] = "Mon 11 am";
       courses[2][2] = "Patel";
       courses[3][0] = "MKT100";
       courses[3][1] = "Tues 8:30 am";
       courses[3][2] = "Wong";
       courses[4][0] = "ACC150";
       courses[4][1] = "Tues 6 pm";
       courses[4][2] = "Deitrich";
       courses[5][0] = "CIS101";
       courses[5][1] = "Fri 1 pm";
       courses[5][2] = "Lennon";
       Scanner sc = new Scanner(System.in);

       String input;
       input = sc.nextLine();

       for(int i = 0; i < 6; i++){
           if(courses[i][0].equals(input)){
               System.out.println(input + " " + courses[i][1] + " " + courses[i][2]);
           }
       }
       if(!(input.equals("CIS101") || input.equals("MKT100") || input.equals("ACC150"))){
           System.out.println("Invalid Entry: No Such course");
       }

   }
}
   
