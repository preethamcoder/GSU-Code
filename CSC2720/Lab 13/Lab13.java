import java.util.*;

public class Lab13 {
    public static void main(String[] args){
        String str = "I like queues but queues do not like me";
        ArrayList<String> toIgnore = new ArrayList<String>();
        toIgnore.add("queues");
        System.out.println(getMostCommonWord(str, toIgnore)); //Should return "like"
    }

    public static String getMostCommonWord(String str, List<String> toIgnore){
        HashMap<String, Integer> map = new HashMap<>();
        String arr[] = str.split(" ");
        int most_freq = -1;
        String res = "";
        for(int i = 0; i < arr.length; i++){
            String key = arr[i];
            if(map.containsKey(key)){
                int value = map.get(key);
                value++;
                if(value > most_freq && (!toIgnore.contains(key))){
                    most_freq = value;
                    res = key;
                }
                map.put(key, value);
            }else{
                map.put(key, 1);
            }
        }
        return res;
    }
}