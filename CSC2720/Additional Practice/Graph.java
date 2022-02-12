public class Graph{
    boolean mat[][];
    int vert;
    public Graph(int ver){
        vert = ver;
        mat = new boolean[vert][vert];
    }
    public void addedge(int i, int j){
        mat[i][j] = true;
        mat[j][i] = true;
    }
    public void removeedge(int i, int j){
        mat[i][j] = false;
        mat[j][i] = false;
    }
}