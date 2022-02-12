package csc1302;

public class StudentClient {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Undergraduate Alex = new Undergraduate("CS", 3.9, 54, true);
		Graduate Mary = new Graduate("Master", 1, 3.91, "Computer Science", "Data science");
		Exchange YingShu = new Exchange(4.0 , "Computer Science", "Tiawan", "Fall 2020");
		System.out.println("Alex: ");
		System.out.println(Alex);
		System.out.println();
		System.out.println("Mary: ");
		System.out.println(Mary);
		System.out.println();
		System.out.println("YingShu: ");
		System.out.println(YingShu);
	}
}
