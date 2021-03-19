package csc1302;
import java.util.*;
/**
 * @author Preetham Thelluri
 *
 */
public class Recursiveproduct {
	public static int product(int x, int y) {
		if(y == 0) {
			return 0;
		}else {
			return(x + product(x, y-1));
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int m, k;
		System.out.println("Enter the values of m and k: ");
		m = sc.nextInt();
		k = sc.nextInt();
		System.out.println("The product is: " + product(m, k));
	}

}
