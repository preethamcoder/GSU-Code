public class LinkedList { 

	static Node head; 

	static class Node { 

		int data; 
		Node next; 

		Node(int d) //Node Constructor
		{ 
			data = d; 
			next = null; 
		} 
	} 

	/* Function to reverse the linked list */
	Node reverse(Node node) 
	{ 
		//Write Your Code Here
        Node current = node;
        Node previous = null;
        
        do{
           Node next = current.next;
            current.next = previous;
            previous = current;
            current = next;
        }while(current != null);
        
        return previous;
	} 

	// prints content of double linked list 
	void printList(Node node) 
	{ 
		//Write Your Code Here
        Node snode = node; 
		while (snode != null) 
		{ 
			System.out.print(snode.data+" "); 
			snode = snode.next; 
		}
	} 

	public static void main(String[] args) 
	{ 
		LinkedList list = new LinkedList(); 
		list.head = new Node(1); 
		list.head.next = new Node(2); 
		list.head.next.next = new Node(3); 
		list.head.next.next.next = new Node(4); 

		System.out.println("Given Linked list"); 
		list.printList(head); 
		head = list.reverse(head); 
		System.out.println(""); 
		System.out.println("Reversed linked list "); 
		//Write Your Code to print the linked list Here. 
        list.printList(head);
	} 
}
