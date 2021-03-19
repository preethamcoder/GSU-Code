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
            ssn = input.nextLine();
            annualSalary = input.nextDouble();
            dept = input.nextLine();
        }
    @Override
        public void display()
        {
            super.display();
            System.out.println("SSN: "+ ssn + " Salary $" + annualSalary + " Department: " + dept);
        }
}
