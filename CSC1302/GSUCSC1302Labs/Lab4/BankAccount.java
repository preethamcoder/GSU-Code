/**
 * 
 */
package csc1302;

/**
 * @author Preetham Thelluri
 *
 */
public class BankAccount {
	private String name;
	private double balance;
	
	public BankAccount(String naam, double amt) {
		name = naam;
		balance = amt;
}
	public BankAccount() {
		// TODO Auto-generated constructor stub
	}
	public void setName(String numa) {
		if(numa.length() != 0) {	
			name = numa;
		}
	}
	public void setBalance(double mon) {
		if(mon >= 0){	
			balance = mon;
		}
	}
	public void deposit(double amount){
		balance += amount;
	}
	public void withdraw(double amount) {
		if(balance >= amount) {
		balance -= amount;
		}
	}
	public String getName() {
		return name;
	}
	
	public String toString() {
		return(name + ", $" + balance);
	}
	
}
