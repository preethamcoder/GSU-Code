import java.util.*;
public class Queue{
    final int MAX = 1000;
    int base, back;
    int A[] = new int[MAX];
    public Queue(){
        back = -1;
        base = -1;
    }
    public Boolean isEmpty(){
        if(base == -1){
            return true;
        }else{
            return false;
        }
    }
    public Boolean isFull(){
        if(base == 0 && back == MAX-1){
            return true;
        }else{
            return false;
        }
    }
    public void enqueue(int n){
        if(isFull()){
            System.out.println("The queue is full");
        }else{
            if(base == -1){
                base = 0;
            }
            back += 1;
            A[back] = n;
        }
    }
    public int dequeue(){
        int ele;
        if(isEmpty()){
            return -1111111;
        }else{
            ele = A[base];
            if(base >= back){
                base = -1;
                back = -1;
            }else{
                base += 1;
            }
            return ele;
        }
    }
}