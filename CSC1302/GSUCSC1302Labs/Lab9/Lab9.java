package csc1302;

import java.util.Scanner;

public class Lab9 {

	public static int cummulativeSum(int n) {
		if(n <= 1) {
			return n;
		}else {
		return(n + cummulativeSum(n-1));
		}
	}
	public static int fib(int n) {
		if(n <= 1) {
			return n;
		}else {
			return(fib(n-1) + fib(n-2));
		}
	}
	public static void print(int n) {
	     if (n!=0){
		print(n-1);
	     	printNum(n);
		System.out.println();
		}
     }
	public static void printNum(int n){
		if(n!=0){
				printNum(n-1);
				System.out.print(n + n + " ");
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Scanner sc = new Scanner(System.in);
		/*First qeustion:
		 * 2
		 * 2 4
		 * 2 4 6
		 * 2 4 6 8
		 * 2 4 6 8 10*/
		System.out.println("First question: ");
		print(5);
		//int x = sc.nextInt();
		System.out.println("Second question:\ncummulativeSum(3) is " + cummulativeSum(3));
		System.out.println("Third question:\nfib(1) is " + fib(1));
		System.out.println("fib(2) is " + fib(2));
		System.out.println("fib(3) is " + fib(3));
		System.out.println("fib(10) is " + fib(10));
	}

}
