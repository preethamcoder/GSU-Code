package csc1302;

public class Graduate extends Student{
	private String degree;
	private String concentration;
	private int years;
	
	public Graduate(String deg, int yr, double gp, String maj, String conc) {
		super(maj, gp);
		degree = deg;
		years = yr;
		concentration = conc;
	}
	
	public int getYears() {
		return(years);
	}
	public String getConcentration() {
		return(concentration);
	}
	public String toString() {
		return("Major is " + super.getMajor() + " Concentration is " + getConcentration() + " Years spent in Graduate school is " + getYears());
	}
}
