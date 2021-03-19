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
        firstName = input.next();
        System.out.println(firstName);
        lastName = input.next();
        System.out.println(lastName);
        address = input.next();
        System.out.println(address);
        zip = input.next();
        System.out.println(zip);
        phone = input.next();
    }
    public void display()
    {
        System.out.println(firstName + " " + lastName + " " + address + " " + zip + " " + phone);
    }
}
