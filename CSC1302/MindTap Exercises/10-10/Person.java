import java.util.*;
public class Person
{
    String firstName;
    String lastName;
    String address;
    String zip;
    String phone;
    Scanner input = new Scanner(System.in);
    public void setData()
    {
        System.out.println("Enter first name: ");
        firstName = input.next();
        System.out.println(firstName);
        System.out.println("Enter last name: ");
        lastName = input.next();
        System.out.println(lastName);
        System.out.println("Enter address: ");
        address = input.next();
        System.out.println(address);
        System.out.println("Enter zipcode: ");
        zip = input.next();
        System.out.println(zip);
        System.out.println("Enter phone number: ");
        phone = input.next();
    }
    public void display()
    {
        System.out.println(firstName + " " + lastName + " " + address + " " + zip + " " + phone);
    }
}
