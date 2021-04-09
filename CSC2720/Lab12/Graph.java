import java.util.*;
public class Graph {
   int numVertices;
   LinkedList<Integer>[] adjacencyList;
   Graph(int n){
      numVertices = n;
      adjacencyList = new LinkedList[numVertices];
      for(int i=0;i<numVertices;i++){
        adjacencyList[i] = new LinkedList<Integer>();
      }
   }
   void addEdge(Integer src, Integer des){
      this.adjacencyList[src].add(des);
   }
   void printGraph(){
      for(int i=0; i<this.numVertices;i++){
      System.out.println("Adjacency list of vertex : " + i);
      System.out.print(""+i+" : ");
      int j=0;
      for(; j<this.adjacencyList[i].size()-1;j++){
         System.out.print(this.adjacencyList[i].get(j));
         System.out.print(" --> ");
      }
      if(j==adjacencyList[i].size()-1){
         System.out.println(this.adjacencyList[i].get(j));
    }else{
         System.out.println();
    }
      }
   }

   public static Integer[][] generateAdjMatrix(Graph g){
      Integer[][] adjacencyMatrix = new Integer[g.numVertices][g.numVertices];
      for(int row=0; row<adjacencyMatrix.length; row++){
         for(int col=0;col<adjacencyMatrix[row].length; col++){
            adjacencyMatrix[row][col] = 0;
         }
      }
      for(int row=0; row<g.numVertices; row++){
         for(int col=0;col<g.adjacencyList[row].size(); col++){
            adjacencyMatrix[row][g.adjacencyList[row].get(col)] = 1;
         }
      }
      return adjacencyMatrix;
   }
   public static void printMatrix(Integer[][] adjMatrix){
      for(int row=0; row<adjMatrix.length; row++){
         for(int col=0;col<adjMatrix[row].length; col++){
            System.out.print(adjMatrix[row][col]+"");
         }
      System.out.println();
      }
   }
   public static void main(String[] args) {
      // Create a graph of 5 vertices
      Graph g2 = new Graph(5);
      g2.addEdge(0, 1);
      g2.addEdge(0, 4);
      g2.addEdge(0, 3);
      g2.addEdge(2, 0);
      g2.addEdge(3, 2);
      g2.addEdge(4, 3);
      g2.addEdge(4, 1);
      g2.printGraph();
      Integer[][] adjMatrix = generateAdjMatrix(g2);
      printMatrix(adjMatrix);
/* Should print the Matrix:
            01011
            00000
            10000
            00100
            01010
*/
   }
}