public class linkedlist{
    static class Node{
        int value;
        Node next;
        public Node(int val){
            value = val;
            next = null;
        }
    }
    Node head = null;
    public void addN(int val){
        Node temp = new Node(val);
        temp.next = head;
        head = temp;
    }
    void deleteF(){
        if(head == null){
            System.out.println("Head node does not exist.");
        }else{
            Node temp = head;
            temp = head.next;
            head = temp;
        }
    }
    void addL(int val){
        Node temp = head;
        Node addend = new Node(val);
        while(temp.next != null){
            temp = temp.next;
        }
        temp.next = addend;
        temp.next.next = null;
    }
    void delLast(){
        Node temp = head;
        while(temp.next.next != null){
            temp = temp.next;
        }
        temp.next = null;
    }
    int size(){
        Node temp = head;
        int i = 0;
        if(head != null){
            i += 1;
        }else{
            return 0;
        }
        while(temp.next != null){
            i += 1;
            temp = temp.next;
        }
        return i;
    }
    void addLoc(int pos, int ele){
        int i = 0;
        if(pos < 0 || pos > (size()-1)){
            System.out.println("Invalid index");
        }else if(pos == size()-1){
            addL(ele);
        }else if(pos == 0){
            addN(ele);
        }else{
            Node temp = head;
            Node addend = new Node(ele);
            while(i != (pos-1)){
                i += 1;
                temp = temp.next;
            }
            addend.next = temp.next;
            temp.next = addend;
        }
    }
    void delPos(int pos){
        if(pos < 0 || pos > (size()-1)){
            System.out.println("Invalid position");
        }
        int i = 0;
        Node temp = head;
        if(pos == 0){
            deleteF();
        }else if(pos == (size()-1)){
            delLast();
        }else{
            while(i != (pos-1)){
                i += 1;
                temp = temp.next;
            }
            Node n = temp.next.next;
            temp.next = n;
        }
    }
    public void reverse(){
        Node prev = null;
        Node curr = head;
        Node next = null;
        while(curr != null){
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        head = prev;
        //return head;
    }
    public void print(){
		Node temp = head;
		while(temp != null){
			System.out.print(temp.value + " ");
			temp = temp.next; 
		}
		System.out.println();
    }
    public static void main(String[] args) {
        linkedlist list = new linkedlist();
        list.addN(12);
        list.addN(12);
        list.addLoc(1, 10);
        list.addLoc(0, 123);
        list.addLoc(2, 1082);
        list.print();
        list.reverse();
        //list.delPos(0);
        //list.delPos(0);
        list.print();
    }
}