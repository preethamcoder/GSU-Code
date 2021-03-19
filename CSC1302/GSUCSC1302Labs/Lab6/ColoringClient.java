package csc1302;

public class ColoringClient {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ColoringPoint CP_blue = new ColoringPoint(3, 2, "Blue");
		ColoringPoint CP_orange = new ColoringPoint(3, 2, "Orange");
		System.out.println("CP_blue color: " +CP_blue.getColor());
		System.out.println();
		System.out.println("CP_orange color: "+CP_orange.getColor());
		System.out.println();
		System.out.println("CP_blue: " + CP_blue.toString());
		System.out.println();
		System.out.println("CP_orange: " + CP_orange.toString());
		System.out.println();
		System.out.println("CP_blue equals CP_orange: " + CP_blue.equals(CP_orange));
	}

}
