package csc1302;
/*The purpose of this lab is to create objects and use methods of a class.
 * We are implementing the over-ridden toString() method
 * */
public class RectangleClient {
	public static void main(String[] args) {
		Rectangle rect1 = new Rectangle();
		Rectangle rect2 = new Rectangle();	
		rect1.setFields(2, 13, 14, 5);
		rect2.setFields(6, 9, 3, 8);
		System.out.println("rect1: " + rect1.toString());
		System.out.println("rect2: " + rect2.toString());
	}
}
