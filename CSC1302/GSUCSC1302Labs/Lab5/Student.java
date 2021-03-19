package csc1302;

public class Student {
	private String major;
	private double gpa;
	private int creditHours;
	public Student(String maj, double gradp, int credh) {
		major = maj;
		gpa = gradp;
		creditHours = credh;
	}
	public Student(String majo, double gap) {
		major = majo;
		gpa = gap;
	}
	public String getMajor() {
		return(major);
	}
	public double getGPA() {
		return gpa;
	}
	public String getYear() {
		if(creditHours < 32) {
			return("Freshman");
		}else if(creditHours >= 32 && creditHours < 64) {
			return("Sophomore");
		}else if(creditHours >= 64 && creditHours < 96) {
			return("Junior");
		}else {
			return("Senior");
		}
	}
	public String toString() {
		return("Major is " + getMajor() + " GPA is " + getGPA() + " Year is " + getYear());
	}
}
