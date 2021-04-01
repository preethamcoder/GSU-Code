import java.util.*;
class Node{ //Class Node
    int item;
    Node next;
    Node(int d){ //Constructs a node
        item = d;
        next = null;
    }
}
public class popQuiz{
    public static void main(String[] args){
        System.out.println("Pop Quiz Programming");
        Node head = new Node(1); //Sets head of list
        head.next=new Node(2); //Sets second value of List
        head.next.next=new Node(3);  //Sets third value of List
        head.next.next.next=new Node(1); //Sets fourth value of List
        head.next.next.next.next=new Node(2); //Sets fifth value of List
        head = getUnique(head); //Calls the method get unique values in the List
        printLinkedList(head); //Calls the method to print the updated List
    }
    public static Node getUnique(Node head){ //Method to get unique values in a List
        Node temp1 = head; //Creates a temp variable and assigns it to the passed value
        Node temp2 = null; //Creates another temp variable and assigns it to null
        while(temp1 != null && temp1.next != null){ //Makes sure that the passed value and the value following it is not null
            temp2 = temp1; //Assigns the value of temp1 variable to the temp2 variable
            while(temp2 != null && temp2.next != null){ //Makes sure that the current node and the next are not null
                if(temp1.item == temp2.next.item){ //Checks if the values are duplicate
                    temp2.next = temp2.next.next; //Assings the next value to the one after it
                }else{
                    temp2 = temp2.next; //Assigns the current value to the next
                }
            }
            temp1 = temp1.next; //Updates teh temp1 variable and iterates through the list
        }
        return head; //Returns only unique values from the list
    }
    public static void printLinkedList(Node head){ // Method to print the list
        for(Node cur = head; cur != null; cur = cur.next){ //Loop to iterate through the list
            if(cur.next == null){ //Checks if the element after the current is null
                System.out.print(cur.item); //Last element gets printed without the arrow
            }else{
                System.out.print(cur.item + " -> "); //Prints the value of the node
            }
        }
        System.out.println(); //Adds a blank new line
    }
}