package csc1302;

public class Undergraduate extends Student{
	private boolean honors;
	
	public Undergraduate(String maj, double gradep, int credh, boolean hon) {
		super(maj, gradep, credh);
		honors = hon;
	}
	public Undergraduate(String maji, double gapa) {
		super(maji, gapa);
	}
	public boolean isHonors() {
		return honors;
	}
	public String toString() {
		return(super.toString() + " Honors is " + isHonors());
	}
}
