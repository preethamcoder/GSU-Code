/**
 * 
 */
package csc1302;

/**
 * @author Preetham Thelluri
 *
 */
public class BankAccountClient {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String name = "Preetham";
		double bal = 190.00;
		//String nam = "Kyoya";
		//double bala = 10.0;
		BankAccount B1 = new BankAccount(name, bal);
		B1.deposit(500.11);
		System.out.println("Pre-withdrawal: " + B1.toString());
		B1.withdraw(300.10);
		System.out.println("Post-withdrawal: " + B1.toString() + "\n");
		BankAccount B2 = new BankAccount();
		System.out.println(B2);
		B2.setName("Kyoya");
		B2.setBalance(101.19);
		System.out.println();
		System.out.println(B2.toString() + " -- Pre-deposit");
		B2.deposit(700.82);
		System.out.println(B2.toString() + " -- Post-deposit");
	}

}
