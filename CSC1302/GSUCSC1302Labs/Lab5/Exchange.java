package csc1302;

public class Exchange extends Undergraduate{
	private String country;
	private String year;
	
	public Exchange(double gaap, String mej, String countr, String yeara) {
		super(mej, gaap);
		country = countr;
		year = yeara;
	}
	public String getYear() {
		return(year);
	}
	public String getCountry() {
		return(country);
	}
	public String toString() {
		return("GPA is " + super.getGPA() + " Major is " + super.getMajor() + " Country is " + getCountry());
	}
}
