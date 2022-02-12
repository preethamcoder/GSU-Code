package csc1302;

public class pattern1c {

	public static void main(String[] args) {
		int x = 5;
		for(int i = x; i >= 1; i--)
		{
		for(int j = x; j >= i; j--) 
		{
		System.out.print(j + " ");
		}
		System.out.println();
		}}}
