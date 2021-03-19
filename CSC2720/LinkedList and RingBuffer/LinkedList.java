public class LinkedList{ //This is the header of the class, it creates the LinkedList class
	static class Node{ //This is the header of the Node class, another class inside the LinkedList class
		int data; //This hold the data in the node
		Node next; //This hold the pointer of the node - the "next" connection
		public Node(int d){ //This is the constructor of the class, it helps to create new nodes and eventually a whole linked list
			data = d; //Assigns the passed parameter to the node's data field
			next = null; //Sets the next pointer of this node as null  
		}
	}
	public Node head = null; //This created a new node called head, and it is currently null, with no initialized data
	
	public void add(int n){ //This method attempts to add a value to the linked list (essentially making a node), it takes an integer as a parameter to add to the data field of the node
		Node temp = new Node(n); //This creates a new temp node with a data value of n
		temp.next = head; //The next pointer of this temp node is set to the head node
		head = temp; //The value of the temp node is being assigned to the head, as a new element has been added. The latest element added would be the head of the list
		//This method has a O(1), CONSTANT run time complexity
	}

	public void deleteHead(){ //This method attempts to delete the head of the linked list
		int num = 0; //This is a variable
		int i = 0; //This is a variable I have defined in advance to use as an iterator in the while loop, set it to 0
		if(head == null){ //Checks if the head is null
			return; //Returns nothing if the head is null, as there is nothing to delete
		}
		Node temp = head; //Creates a new node temp with the head as the value, as the head is not null
		if(num == 0){ //Checks if the value of num is 0
			head = temp.next; //In the event that the value of num is 0, 
			return; //Returns nothing after that, as the pointer has been moved and there would only be one element to delete
		}
		while(temp != null && i < num - 1){ //Checks if the temp node is not null and if the iterator is less than -1
			temp = temp.next; //Keeps moving the pointer of the node to the left as long as the current node is not null and the iterator is less than -1
			i += 1; //Increases the iterator variable by 1 to avoid getting caught in a infinite loop
		}
		if(temp == null || temp.next == null){ //Checks if the current node or the node after it are null
			return; //In the event that either or both are true, it exits this method, as it would either be an empty linked list or want to delete only the first or last node.
		}
		Node next = temp.next.next; //This shifts the nodes to the left and assigns the next node as two nodes after the current node
		temp.next = next; //The next node is being assigned as a pointer to the SUCCESSOR of the current node.
		//This method has a Linear runtime complexity in the worst case - O(n)
	}

	public void print(){ //This method attempts to print the data contained in all the nodes of the linked list, node by node
		Node temp = head; //This creates a temporary node, which is equated to the head of the linked list
		while(temp != null){ //This keeps moving through every node in the linked list, as long as it is not null (until it approaches the last element before the null element)
			System.out.print(temp.data + " "); //This prints out the data/value held in each node, along with a space
			temp = temp.next; //The temp node is given the value of its next node, in order to access the subsequent elements, one after the other 
		}
		System.out.println(); //This prints a blank line to avoid pushing everything on one line and making things clumsy
		//This method has a Linear - O(n) - runtime complexity
	}

	public void printHead(){ //This method attempts to print the head of the list
		System.out.println(head.data); //This statement prints out the value of the head node in the linked list
		//This has a constant runtiem complexity - O(1)
	}

	public static void main(String[] args) { //This is the main method/driver, it shows how the Node and LinkedList class would work in a practical scenario
		LinkedList list = new LinkedList(); //This creates a new linked list called list, which would be able to hold values and pointers
		list.add(1); //This attempts to push the value 1 to the linked list by invoking the add method
		list.add(2); //This attempts to push the value 2 to the linked list by invoking the add method
		list.add(3); //This attempts to push the value 3 to the linked list by invoking the add method
		list.add(4); //This attempts to push the value 4 to the linked list by invoking the add method
		list.add(5); //This attempts to push the value 5 to the linked list by invoking the add method
		System.out.print("The list is: "); //This prints out a string to set up the list that follows and increase the readablity of the output
		list.print(); //This attempts to print out the values (data) in the linked list by invoking the print method
		System.out.print("The head element of this list is: "); //This prints out a string to set up the head of the list that follows and increase the readablity of the output
		list.printHead(); //This attempts to print out the head node value of the linked list by invoking the printHead() method 
		list.deleteHead(); //This attempts to delete the current head of the linked list by invoking the deleteHead() method
		System.out.print("The list after deleting the head is: "); //This prints out a string to set up the list (after deleting the head) that follows and increase the readablity of the output
		list.print(); //This attempts to print out the values (data) in the linked list by invoking the print method - after the head has been deleted
		System.out.print("The new head is: "); //This prints out a string to set up the new head of the list, increasing the readablity of the output
		list.printHead(); //This attempts to print out the new value of the head node of the linked list by invoking the printHead() method
	}
	//This has a Linear runtime complexity - O(n). The runtime is 1.5 milliseconds.
	//This has a Linear space complexity - O(n). The space occupied is 1.8 megabytes.
}
