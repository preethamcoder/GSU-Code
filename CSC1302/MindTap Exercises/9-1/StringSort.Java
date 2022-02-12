import java.util.*;
import java.util.Arrays;
public class StringSort
{
   public static void main(String[] args)
   {
      String[] values =  {"mouse", "dog", "cat", "horse", "cow",
         "moose", "tiger", "lion", "elephant", "bird", "hamster",
         "guinea pig", "leopard", "aardvark", "hummingbird"};       
         for(int i = 0; i < values.length-1; i++){
             for(int j = i+1; j < values.length; j++){
                 if((values[i].compareTo(values[j]))>0){
                     String a = values[i];
                     values[i] = values[j];
                     values[j] = a;
                 }
   }
}
System.out.println(Arrays.toString(values));
}
}
