package csc1302;
import java.util.*;
import java.util.Arrays;
import java.util.Collections;
public class Lab8Client {

	public static void main(String[] args) {
		ArrayList<Rectangle> list1 = new ArrayList<Rectangle>(Arrays.asList(
				new Rectangle(91,10, new Point(0,0)),
				new Rectangle(19,10, new Point(1,1)),
				new Rectangle(28,9, new Point(1,2)),
				new Rectangle(72,7, new Point(3,1)),
				new Rectangle(16,6, new Point(4,3)),
				new Rectangle(51,5, new Point(2,7)),
				new Rectangle(52,4, new Point(1,9)),
				new Rectangle(34,3, new Point(6,8)),
				new Rectangle(22,2, new Point(10,2)),
				new Rectangle(111,1, new Point(2,3))
				));
		System.out.println(list1);
		Collections.sort(list1);
		//Collections.sort(list1);
		System.out.println("Sorted List:");
		System.out.println(list1);

	}

}
