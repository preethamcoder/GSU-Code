import java.util.*;
public class Lab4 {
public static void main (String[] args){
    Scanner sc = new Scanner(System.in); //Declared a scanner
    System.out.println("Enter a string"); //Asking the user to enter the string to be checked
    String s1 = sc.nextLine(); //The given test string
    boolean ans = checkPalindrome(s1); //The method to check for pallindrome
    System.out.println(ans); // Should be True
}
public static boolean checkPalindrome(String s1){ 
    // Example of stack	push	s.push("r")
    // Example of	stack	pop	s.pop()
    // Example of	queue enqeue	q.add("r")
    //	Example of queue dequeue	q.poll()
    //	Check if stack or queue is empty	s.isEmpty() , q.isEmpty()
    //	INSERT YOUR CODE HERE
    Stack<Character> s = new Stack<Character>(); //A stack to hold the contents of the string in reverse order
    Queue<Character> q = new LinkedList<Character>(); //A queue to hold the contents of the string in conventional order
    String srev = ""; //Place holder for reversed stack string
    String qrev = ""; //Place holder for the straight queue string
    for(int i = 0; i < s1.length(); i++){ 
        s.push(s1.charAt(i)); //Populating the stack character by character
        q.add(s1.charAt(i)); //Populating the queue character by characer
    }
    while(!(s.isEmpty())){
        srev += s.pop(); //Populating the reverse string with the contents of the stack
    }
    while(!(q.isEmpty())){
        qrev += q.poll(); //Populating the straight string with the contents of the queue
    }
    //return(srev.equals(qrev)); This is an alternate method of telling if the string is a pallindrome
    return ((s1.toLowerCase()).equals(srev.toLowerCase()) && (s1.toLowerCase()).equals(qrev.toLowerCase())); //Here, I am comparing the strings and telling if they are all the same.
    }
}
