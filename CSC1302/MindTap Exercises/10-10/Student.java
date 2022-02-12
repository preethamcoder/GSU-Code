import java.util.*;
public class Student extends Person
{
    private String major;
    private double gpa;
    Scanner input = new Scanner(System.in);
    @Override
        public void setData()
        {
            super.setData();
            System.out.println("Enter major: ");
            major = input.nextLine();
            System.out.println("Enter GPA: ");
            gpa = input.nextDouble();
        }
    @Override
        public void display()
        {
            super.display();
            System.out.println("Major: " + major + "  GPA: " +gpa);
        }
}
