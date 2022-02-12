import java.util.*;
public class Lab2{
public static void main(String[]args){
    String str = "{}{{{{}}";
    boolean ans = isbalanced(str);
    System.out.println("Answer "+ ans); // Should be False

}

public static boolean isbalanced(String str){ 
    Stack<Character> stack = new Stack<Character>();
    // Example of push	stack.push("{")
    // Example of pop	stack.pop()
    // Example of isEmpty stack.isEmpty()
    // INSERT YOUR CODE HERE
    for(int i = 0; i < str.length(); i++){
        char bracket = str.charAt(i);
        if(bracket == '{'){ //I am checking for an opening brace and pushing it into the stack.
            stack.push(bracket);
        }else if(stack.isEmpty()){ //If the bracket is not an opening one and there are no elements in the stack, it is not balanced.
            return false;
        }else if(bracket == '}'){ //I am popping one opening brace everytime I see a closing brace, this helps me keep track of even stacks.
            stack.pop();
        }
    }
    return stack.isEmpty(); //At the end, after all braces are considered, if the stack still has elements, then the stack is not balanced. 
    }
}
