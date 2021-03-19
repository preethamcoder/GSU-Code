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
            major = input.nextLine();
            gpa = input.nextDouble();
        }
    @Override
        public void display()
        {
            super.display();
            System.out.println("Major: " + major + "  GPA: " +gpa);
        }
}
