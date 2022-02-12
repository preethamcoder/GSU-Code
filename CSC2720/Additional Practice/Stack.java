import java.util.*;
public class Stack{
    final int MAX = 1000;
    int top;
    int A[] = new int[MAX];
    public Stack(){
        top = -1;
    }
    public boolean isEmpty(){
        if(top >= 0){
            return(true);
        }else{
            return(false);
        }
    }
    public boolean push(int x){
        if(top > (MAX-1)){
            return false;
        }else{
            top += 1;
            A[top] = x;
            return true;
        }
    }
    public String pop(){
        if(top < 0){
            return("Cannot pop element");
        }else{
            String x = (String.valueOf(A[top--]));
            return(x);
        }
    }
    public static void main(String[] args) {
        Stack s = new Stack();
        s.push(10);
        s.push(20);
        s.push(30);
        System.out.println(s.pop() + " is the popped element.");
    }
}