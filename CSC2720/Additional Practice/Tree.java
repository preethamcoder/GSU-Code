public class BinaryTree{
    static class Node{
        int value;
        Node left;
        Node right;
        public Node(int val){
            value = val;
            right = null;
            left = null;
        }
    }
    Node root;
    public Node addR(Node curr, int val){
        if(curr == null){
            return new Node(val);
        }
        if(val < curr.value){
            curr.left = addR(curr.left, value);
        }else if(val > curr.value){
            curr.right = addR(curr.right, value);
        }else{
            return curr;
        }
    }
    public void add(int val){
        root = addR(root, val);
    }
    public Boolean containsN(Node curr, int val){
        if(curr == null){
            return false;
        }
        if(curr.value == val){
            return true;
        }
        if(val < curr.value){
            return containsN(curr.left, val);
        }else{
            return containsN(curr.right, val);
        }
    }
    public Boolean containsNode(int val){
        return containsN(root, val);
    }
    public int find_Small(Node root){
        if(root.left == null){
            return root.value;
        }else{
            find_Small(root.left);
        }
    }
    public void get(int val){
        System.out.println(" "+val);
    }
    public Node deleteR(Node curr, int val){
        if(curr == null){
            return null;
        }if(val == curr.value){
            return curr.left;
        }if(curr.value == val){
            return curr.right;
        }else{
            int minval = find_Small(curr.right);
            curr.value = minval;
            curr.right = deleteR(curr.right, minval);
            return curr;
        }
    }
    public void preOrder(Node n){
        if(n != null){
            get(n.value);
            preOrder(n.left);
            preOrder(n.right);
        }
    }
    public void postOrder(Node n){
        if(n != null){
            postOrder(n.left);
            postOrder(n.right);
            get(n.value); 
        }
    }
    public inOrder(Node n){
        if(n != null){
            inOrder(n.left);
            get(n.value);
            inOrder(n.right);
        }
    }
}