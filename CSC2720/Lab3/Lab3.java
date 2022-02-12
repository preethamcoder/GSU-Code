import java.util.*;
public class Lab3 {
public static void main (String[] args){ String
s1 = "DataStructuresIssss###Fun"; String
s2 = "DataStructuresIszwp###Fun"; boolean
ans = backspaceCompare(s1,s2);
System.out.println(ans); // Should be True
}
public static boolean backspaceCompare(String s1, String s2){
    Stack<Character> s1_stack = new Stack<Character>();
    Stack<Character> s2_stack = new Stack<Character>();
// Example of push
// Example of peek
// Example of pop
// Example of isEmpty
//stack.push("D");
//stack.peek();
//stack.pop();
//stack.isEmpty();
// INSERT YOUR CODE HERE
    //char[] s1_arr = s1.toCharArray(); //Converts first string to array
    //char[] s2_arr = s2.toCharArray(); //Converts second string to array

    for(int i = 0; i < s1.length(); i++){
        char ch = s1.charAt(i); //Takes character by character of first array
        if(ch != '#'){ 
            s1_stack.push(ch); //Pushes the character to the stack
        }else if(!s1_stack.empty()){
            s1_stack.pop(); //Removes the character if # is typed
        }
    }

    for(int j = 0; j < s2.length(); j++){
        char ar = s2.charAt(j); //Takes character by character of second array
        if(ar != '#'){
            s2_stack.push(ar); //Pushes a character to the stack
        }else if(!s2_stack.empty()){
            s2_stack.pop(); //Removes a character if # is typed
        }
    }

    String res1 = String.valueOf(s1_stack); //Converts the array to String
    String res2 = String.valueOf(s2_stack); //Converts the arry to String
    return res1.equals(res2); //Compares the two strings and returns a value
}
}
