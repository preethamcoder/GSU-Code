import java.util.*;
public class CollegeCourse
{
   String dept;
   int id;
   double credits;
   double pay = 0.0;
   double price;
   public CollegeCourse(String depart, int identity, double cred){
       dept = depart;
       id = identity;
       credits = cred;
       price = 120 * credits;
   }
   
   public void display(){
       System.out.println(dept+id+ "\n"+ "Non-lab course" + "\n" + credits + " credits" + "\n" + "Total fee is $" + price);
   }
   
}

import java.util.*;
public class LabCourse extends CollegeCourse
{
   private double labFee = 50.0;

   public LabCourse(String cn, int iden, int cerda){
       super(cn, iden, (double) cerda);
       super.price += labFee;
   }
   //double pay = credits * 120 + 50.0;
   public void display(){
       System.out.println(super.dept+super.id+ "\n"+ "Lab course" + "\n" + super.credits + " credits" + "\n" + "Lab fee is $" + (int) labFee + "\n" + "Total fee is $" + (super.price + labFee));
      
}
}

import java.util.*;
public class UseCourse
{
   public static void main(String[] args)
   {
      Scanner input = new Scanner(System.in);
      String dept, inStr;
      String[] labCourses = {"BIO", "CHM", "CIS", "PHY"};
      int id, credits;
      int found = 0;
      int x;
      
      // your code here

      
   }
}
