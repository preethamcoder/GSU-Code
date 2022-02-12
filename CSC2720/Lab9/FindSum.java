import java.util.*;
public class FindSum{
    public static void main(String[] args) {
        int[] arr = { 1, 5, 4, 6, 7, 9 }; 
        HashSet<Integer> res = findSums(arr); 
        System.out.println(res.toString());
    }
    public static HashSet<Integer> findSums(int[] array){
        HashSet<Integer> sums = new HashSet<Integer>();
        HashSet<Integer> table = new HashSet<Integer>();
        // To Initialize	a hashtable	HashSet<Integer> hashtable = new HashSet<Integer>();
        //	To	add "newItem" to hashtable			hashtable.add(newItem);
        //	To	check if "item" exist in hashtable	hashtable.contains(item);					
        for(int i = 0; i < array.length; i++){
            for(int j = 0; j < array.length; j++){
                if(!(table.contains(array[j]))){
                    table.add(array[j]);
                }
                if(table.contains(array[i]+array[j])){
                    sums.add(array[i]+array[j]);
                }
            }
        }
        return sums;
    }
}
