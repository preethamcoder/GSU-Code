import java.util.*;
public class TryToParseDouble {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        try{
            double da = Double.parseDouble(a);
            System.out.println(da);
        }catch(NumberFormatException mistake){
            a = "0.0";
            System.out.println(a);
            System.out.println("Value entered cannot be converted to a floating-point number.");
        }
    }
}
