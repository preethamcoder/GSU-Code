import java.util.*;
class Node { 
	int data; 
	Node left, right; 
	Node(int d) 
	{ 
		data = d; 
		left = right = null; 
	} 
} 
class BinarySearchTree { 
	// Root of BST 
	Node root; 
	// Constructor 
	BinarySearchTree() 
	{ 
		root = null; 
	} 
	// function to insert nodes 
	public void insert(int data) 
	{ 
		this.root = this.insertRec(this.root, data); 
	} 
	/* A utility function to insert a new node 
	with given key in BST */
	private Node insertRec(Node node, int data) 
	{ 
		if (node == null) { 
			this.root = new Node(data); 
			return this.root; 
		} 
		if (data == node.data) { 
			return node; 
		}else if(data < node.data) { 
			node.left = this.insertRec(node.left, data); 
		} else { 
			node.right = this.insertRec(node.right, data); 
		} 
		return node; 
	}
	// class that stores the value of count 
	public class count { 
		int c = 0; 
	} 
	// utility function to find kth largest no in a given tree 
	void kthLargestUtil(Node node, int k, count C) 
	{ 
		// Base cases, the second condition is important to 
		// avoid unnecessary recursive calls 
		if (node == null || C.c >= k) 
			return; 
		this.kthLargestUtil(node.right, k, C); 
		C.c++; 
		if (C.c == k) { 
			if(k == 1){
				System.out.println(k + "st largest element is " + node.data);
				return;
			}else if(k == 2){
				System.out.println(k + "nd largest element is " + node.data);
				return;
            }else if(k == 3){
                System.out.println(k + "rd largest element is " + node.data);    
			}else{
				System.out.println(k + "th largest element is " + node.data); 
				return; 
			}
		} 
		this.kthLargestUtil(node.left, k, C); 
	} 
	// Method to find the kth largest no in given BST 
	void kthLargest(int k) 
	{ 
		count c = new count();
		this.kthLargestUtil(this.root, k, c); 
	} 
	// Driver function 
	public static void main(String[] args) 
	{ 
		BinarySearchTree tree = new BinarySearchTree(); 
		Scanner sc = new Scanner(System.in);
		tree.insert(50); 
		tree.insert(30); 
		tree.insert(20); 
		tree.insert(40); 
		tree.insert(70); 
		tree.insert(60); 
		tree.insert(80); 
		System.out.print("Enter the k value: ");
		int k = sc.nextInt();
		tree.kthLargest(k);		
	} 
}
