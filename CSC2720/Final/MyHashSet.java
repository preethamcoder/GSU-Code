import java.util.*; //Importing all the packages in the java.util library
class MyHashSet { //Class to create a hashset without using the hashset library
    List<Integer>[] hashSet; //Global variable to save the hashset in a list
    public int getPos(int key, int index) { //Method to extract the position of the given key and index
        List<Integer> pos = hashSet[index]; //Creates a temporary list 
        int res = -1; //Variable to store position
        if (pos == null) { //Checks if the position exists in the list
            return res; //Returns -1 if the condition is true
        }
        int size = pos.size(); //Saves the size of the list in size
        for (int i = 0; i < size; ++i) { //Iterates through the list to find the key
            if (pos.get(i) == key) { //Checks if the element here is the same as the key
                res = i; //Saves the position to the variable
                break; //Exits the loop if the position is found
            }
        }
        return res; //Returns the position
    }
    public int getIndex(int key) { //Method to extract the index of the passed key
        return key % 100; //Assuming the size is 100, this gets a "modulo 100" of the key
    }
    public MyHashSet() { //Constructor of the MyHasSet class
        hashSet = (List<Integer>[]) new ArrayList[100]; //Creates and casts a new array list to serve the purpose of the program
        //Size is 100
    }
    public void insert(int key) { //Method to add a value into the hashset
        int index = getIndex(key); //Gets the index of the key
        int pos = getPos(key, index); //Gets the position to store the key
        if (pos < 0) { //Checks if the position exists
            if (hashSet[index] == null) { //Checks if the set is null
                hashSet[index] = new ArrayList<Integer>(); //Creates an arraylist if it is null
            }
            hashSet[index].add(key); //Otherwise adds the key to the set
        }
    }
    public void contains(int key) { //Method to check if the key is in the set
        int index = getIndex(key); //Gets the index of the key
        int pos = getPos(key, index); //Gets the position of the key
        if(pos >= 0){ //Checks if the position exists
            System.out.println(key); //Prints the integer if the position exists
            System.out.println("True"); //Confirms the existence of the element
        }else{
            System.out.println("Hey Nothing there"); //Otherwise prints that the key does not exist
        }
    }
    public void remove(int key) { //Method to remove the passed key
        int index = getIndex(key); //Gets the index of the key
        int pos = getPos(key, index); //Gets the position to remove
        if (pos >= 0) { //Checks if the position exists in the set
            hashSet[index].remove(pos); //Removes the position where the key was stored
            System.out.println("Removed"); //Confirming the removal
        }else{
            System.out.println("Hey value does not exist at all"); //Signifies that the value doesn't exist
        }
    }
    public static void main(String[] args) { //Main Method
        long startime = System.nanoTime();//Variable to hold the start time
        MyHashSet hashSet = new MyHashSet(); //Intializes the hashset
        hashSet.insert(1); //Adds 1. Set = 1
        hashSet.insert(2); //Adds 2. Set = 1, 2
        hashSet.insert(10); //Adds 10. Set = 1, 2, 10
        hashSet.remove(2); //Removes 2. Set = 1, 10
        hashSet.contains(1); //Checks if the set contains 1. Should return 1
        hashSet.insert(3); //Adds 3. Set = 1, 10, 3
        hashSet.contains(2); //Checks if the set contains 2. Should print "Hey Nothing there".
        hashSet.remove(5); //Tries to remove 5. Set = 1, 10, 3. Should print "Hey value does not exist at all"
        long endtime = System.nanoTime(); //Variable to store the end time
        System.out.println("Time taken to run the code: " + (endtime - startime) + " ms"); //Computes the time taken to run
        /* OUTPUT:
            Removed 
            1
            True
            Hey Nothing there
            Hey value does not exists at all
            Time taken to run the code: <value> ms
        */
    }
}
//Time Complexity: O(n)
//Space Complexity: O(n)
