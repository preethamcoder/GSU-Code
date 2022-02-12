import java.util.*;
public class arrayrotate {
    public static void rotate(double[] a1, int n){
        if(n > a1.length){
            System.out.println("There are not enough elements to rotate this array.");
        }else if(n == a1.length){
            System.out.println("Rotated array is: " + Arrays.toString(a1));
        }else{
            double[] newarr = new double[a1.length];
            for(int i = 0; i < a1.length-n; i++){
                newarr[i] = a1[i+n];
            }
            for(int j = a1.length-1; j > a1.length-n-1; j--){
                newarr[j] = a1[j-a1.length+n];
            }
            System.out.println("Rotated array is: " + Arrays.toString(newarr));
        }
    }
    public static void main(String[] args) {
        int a, ele;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of elements in your array: ");
        a = sc.nextInt();
        System.out.println("Enter the elements of the array one after the other: ");
        double array[] = new double[a];
        for(int i = 0; i < a; i++){
            array[i] = sc.nextDouble();
        }
        System.out.println("Original array is: " + Arrays.toString(array));
        System.out.println("How many elements do you want to rotate the array by? ");
        ele = sc.nextInt();
        rotate(array, ele);
        sc.close();
    }    
}
