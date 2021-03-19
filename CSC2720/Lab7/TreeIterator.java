import java.util.LinkedList;

public class TreeIterator<T> implements java.util.Iterator<T> {
private BinaryTreeBasis<T> binTree;
  private TreeNode<T> currentNode;
  private LinkedList <TreeNode<T>> queue; // from JCF

  public TreeIterator(BinaryTreeBasis<T> bTree) {
    binTree = bTree;
    currentNode = null; 
    // empty queue indicates no traversal type currently 
    // selected or end of current traversal has been reached
    queue = new LinkedList <TreeNode<T>>();
  }  // end constructor

  public boolean hasNext() {
    return !queue.isEmpty();
  }  // end hasNext

  public T next() 
           throws java.util.NoSuchElementException {
      currentNode = queue.remove();
      return currentNode.getItem();
  }  // end next

  public void remove() 
              throws UnsupportedOperationException {
    throw new UnsupportedOperationException();
  }  // end remove

  public void setPreorder() {
    queue.clear();
    preorder(binTree.root);
  }  // setPreOrder

  public void setInorder() {
    queue.clear();
    inorder(binTree.root);
  }  // end setInorder

  public void setPostorder() {
    queue.clear();
    postorder(binTree.root);
  }  // end setPostorder

  private void preorder(TreeNode<T> treeNode) {
    if (treeNode != null) {  
      queue.add(treeNode);
      preorder(treeNode.getLeft());
      preorder(treeNode.getRight());
    } // end if
  }  // end preorder

  private void inorder(TreeNode<T> treeNode) {
    if (treeNode != null) {  
      inorder(treeNode.getLeft());
      queue.add(treeNode);
      inorder(treeNode.getRight());
    } // end if
  }  // end inorder

  private void postorder(TreeNode<T> treeNode) {
    if (treeNode != null) {  
      postorder(treeNode.getLeft());
      postorder(treeNode.getRight());
      queue.add(treeNode);
    } // end if
  }  // end postorder
}  // end TreeIterator