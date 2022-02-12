/**
 * 
 */
package csc1302;
import java.util.*;
/**
 * @author sthelluri1
 *
 */
public class Lab7 {
	
	public static void removeOddLength(ArrayList<String> ala) {
		for(int i = 0; i < ala.size(); i++) {
			if((ala.get(i)).length() % 2 != 0) {
				ala.remove(i);
			}
		}
		System.out.println("Array after removeOddLength method: " + ala);
	}
	public static void swapPairs(ArrayList<String> ala2) {
		if(ala2.size() % 2 == 1) {
			for(int i = 0; i < ala2.size()-1; i += 2) {
				String temp = ala2.get(i);
				ala2.set(i, ala2.get(i+1));
				ala2.set(i+1, temp);
			}
		}else {
			for(int i = 0; i < ala2.size()-1; i += 2) {
				String temp = ala2.get(i);
				ala2.set(i, ala2.get(i+1));
				ala2.set(i+1, temp);
			}
		}
		System.out.println("After swapPairs method: " + ala2);
	}
	public static void intersect(ArrayList<Integer> lia1, ArrayList<Integer> lia2) {
		ArrayList<Integer> gon = new ArrayList<Integer>();
		if(lia1.size() <= lia2.size()) {
			for(int i = 0; i < lia1.size(); i++) {
				for(int x = 0; x < lia2.size(); x++) {
					if(lia1.get(i) == lia2.get(x)) {
						gon.add(lia2.get(x));
					}
				}
			}
		}else {
			for(int i = 0; i < lia2.size(); i++) {
				for(int x = 0; x < lia1.size(); x++) {
					if(lia2.get(i) == lia1.get(x)) {
						gon.add(lia1.get(x));
					}
				}
			}
		}
		System.out.println("Intersection of " + lia1 + " and " + lia2 + " is " + gon);
	}
	
	public static void main(String[] args) {
		
		ArrayList<String> alist = new ArrayList<String>();
		alist.add("Draco");
		alist.add("Juan");
		alist.add("Kanto");
		alist.add("Unnova");
		alist.add("Gon");
		alist.add("Strike");
		System.out.println("Original array: " + alist);
		ArrayList<String> alist2 = new ArrayList<String>();
		alist2 = alist;
		ArrayList<Integer> type1 = new ArrayList<Integer>();
		type1.add(1);
		type1.add(4);
		type1.add(8);
		type1.add(9);
		type1.add(11);
		type1.add(15);
		type1.add(17);
		type1.add(28);
		type1.add(41);
		type1.add(59);
		ArrayList<Integer> type2 = new ArrayList<Integer>();
		type2.add(4);
		type2.add(7);
		type2.add(11);
		type2.add(17);
		type2.add(19);
		type2.add(20);
		type2.add(23);
		type2.add(28);
		type2.add(37);
		type2.add(59);
		type2.add(81);
		swapPairs(alist2);
		removeOddLength(alist);
		intersect(type1, type2);
		//ArrayList<String> alist2 = new ArrayList<String>();
		
		
		
		

	}

}
