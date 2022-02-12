import java.util.*;
public class Lab10 {
    public static void main(String []args){
        int[] arr = {1, 5, 3, 4, 2};
        int k = 3;
        long start = System.currentTimeMillis();
        System.out.println("Count is "+ solve_with_Hash(arr,k)); //should be 2 
        System.out.println("Total execution time (taken by solve_with_Hash): " + (System.currentTimeMillis()-start));
        start = System.currentTimeMillis();
        System.out.println("\n\nCount is "+ solve_with_Sort(arr,k)); //should be 2 
        System.out.println("Total execution time (taken by solve_with_Sort): " + (System.currentTimeMillis()-start));
    }
    public static int solve_with_Sort(int[] arr, int k){ 
        int count = 0;
        Arrays.sort(arr);
        int lf = 0, rt = 0;
        while(rt < arr.length){
            int df = arr[rt] - arr[lf];
            if(df == k){
                count++;
                lf++;
                rt++;
            }else if(df > k){
                lf++;
            }else{
                rt++;
            }
        }
        return count;
    }
    public static int solve_with_Hash(int[] arr, int k){ 
        int count = 0;
        HashSet<Integer> hash = new HashSet<Integer>();
        for(int i = 0; i < arr.length; i++){
            int key = arr[i];
            hash.add(key);
        }
        for(int i = 0; i < arr.length; i++){
            if(hash.contains(arr[i] + k) || hash.contains(arr[i] - k)){
                count++;
                hash.remove(arr[i]);
            }
        }
        return count;
    }
}