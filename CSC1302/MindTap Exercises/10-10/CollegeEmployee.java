import java.util.*;
public class CollegeEmployee extends Person
{   
    private String ssn;
    private double annualSalary;
    private String dept;
    Scanner input = new Scanner(System.in);
    @Override
        public void setData()
        {
            super.setData();
            System.out.println("Enter SSN: ");
            ssn = input.nextLine();
            System.out.println("Enter annual salary: ");
            annualSalary = input.nextDouble();
            System.out.println("Enter department: ");
            dept = input.nextLine();
        }
    @Override
        public void display()
        {
            super.display();
            System.out.println("SSN: "+ ssn + " Salary $" + annualSalary + " Department: " + dept);
        }
}
