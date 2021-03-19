public class RingBuffer { //This is the header, creates a class called RingBuffer
    static int buffer[]; //Creates an array called buffer
    private static int length; //Records and keeps track of the length of the array
    private static int front; //Records keeps track of the the element in the first place
    private static int rear; //Records and keeps track of the element in the last place
    private static int curSize; //Records and keeps track of the number of "real" elements in the array, except "-1s."

    public RingBuffer(int length){ //This is the constructor for the class, with a parameter containing the length of the list.
        buffer = new int[length]; //It initializes the buffer array by enabling it to contain the number of elements from the parameters.
        this.length = length; //Sets the length of the buffer array to the passed value
        fill(); //Fills the array with -1s
        rear = -1; //Sets the rear to -1, as the array is empty for now
        front = -1; //Sets the front to -1, as the array is empty for now
        curSize = 0; //As the array only contains -1s now, the size is 0. No elements have been added by the user
    }
    public void add(int element){ //This method helps the user add some elements to the array
        if(curSize == length){ //Checks if the array already has maximum elements. Current size should be equal to length for that
            System.out.println("Buffer is Full"); //If yes, the array is full and can't be added to
        }else{ //This executes if the array is not full
            rear = (rear + 1) % length; //The value of the rare is being updated, it points to the position where the element must be added
            buffer[rear] = element; //The element is being added to the buffer array at the "rear" position
            curSize += 1; //Since a new, valid element has been added, the size of the buffer array increases by 1. There is one more "legal" element in it
            if(front == -1){ //This checks if the element is the first ebing added
                front = rear; //In the event that the element is the first element being added, the front is set to the rear only in that iteration
            }
        }
        //This has a CONSTANT (O(1)) runtime complexity, as there are no loops!
    }
    public void fill(){ //This method fills the array with -1s, before it is being pushed with other elements.
        for(int i = 0; i < buffer.length; i++){ //This creates a set of indices from 0 to one less than the total length of the buffer array. This helps to access each place in the array and populate it with a -1.
            buffer[i] = -1; //This populates each index of the buffer array with a -1. 
        }
        //This has a LINEAR (O(n)) runtime complecity, as there is one 'for' loop! 
    }
    public int delete(){ //This method attempts to delete the first element in the array
        int temp = 0; //Initializes a temp avriable and sets it to 0 for future use
        if(front == -1){ //Checks if front is equal to -1. In the event that front equals -1, the array would be empty
            System.out.println("Buffer is Empty"); //This says that the array is empty if the avlue fo front is -1, as no new elements have been added and none can be deleted
        }else{ //This block of code executes when the array contains some elements and is not empty
            temp = buffer[front]; //This code assigns the value of the the first element in the array to the variable temp, as it is the value to be deleted
            if(front == rear){ //This checks if front and rear have the same value - in the event that they do, it executes the below code
                front = -1; //The value of front is being set to -1, as per the directions
                rear = -1; //The value of rear has been set of -1, same as front, as per the directions
                buffer[0] = -1; //This sets the first element of the array to -1
            }else if(front == length - 1){ //Another condition we were asked to check in the direction, if the front was equal to length-1, which is the last element in the array
                front = 0; //In the event that front is equal to length - 1, front is set to 0, as per the directions.
            }else{ //This rotates the buffer to the left and starts assigning the later values to previous variables
                for(int i = 0; i < buffer.length - 1; i++){ //This for loop creates a set of indices fro the program to access elements of the array, one by one
                    buffer[i] = buffer[i+1]; //The value of the an element is being set to that of it's adjacent neighbor, with the exception of the last element
                }
            }
            buffer[length-1] = -1; //This sets the last value of the last element in the buffer to -1, thus not counting it anymore
            curSize -= 1; //Decrements the size of the array by 1, as one element has been popped off
            rear -= 1; //Decrements the value of rear by one, as one element has been removed, and there is one lesser element in the buffer
        }
        return temp; //Retuns the element that has been deleted
        //In the worst case, this has a Linear runtime complexity - O(n)
    }
    public void printBuffer(){ //This method prints out the buffer array, element by element, as long as it is not empty
        if(front == -1){ //This checks if the front is equal to -1, which implies that no new elements have been added
            System.out.println("Buffer is Empty"); //In the event that no new elements have been added, the buffer array would be empty and we will be notified as such by the program
        }else{ //This block executes in the event that the buffer array is not empty
            System.out.print("Elements in the Ring Buffer are: "); //This is a print statement that sets the context of the array elements to increase the readability of the output
            for(int i = front; i <= rear; i++){ //This creates a new set of indices, starting from the front to the rear of the buffer array. Looping through this would help to access each element in the buffer array
                System.out.print(buffer[i] + " "); //This prints out each element of the array along with an additional space
            }
            System.out.println(); //This prints a blank line to avoid pushing everything on one line and making things clumsy
        }
        //This method has a LINEAR - O(n) - runtime complexity
    }
    public static void main(String[] args){ //This is the main method/driver, it demonstrates how the program works in a practical situation
        RingBuffer arr = new RingBuffer(5); //Creates a ring buffer array with a length of 5
        arr.add(1); //Adds 1 to the buffer array with the add() method
        arr.add(2); //Adds 2 to the buffer array with the add() method
        arr.add(3); //Adds 3 to the buffer array with the add() method
        arr.add(4); //Adds 4 to the buffer array with the add() method
        arr.printBuffer(); //Invokes the printBuffer() method to print out all the elements of the array
        System.out.println("Deleted value = " + arr.delete()); //Invokes the delete() method to delete the first element and prints out the deleted element. Should be 1
        System.out.println("Deleted value = " + arr.delete()); //Invokes the delete() method to delete the (now) first element and prints out the deleted element. Should be 2
        arr.printBuffer(); //Invokes the printBuffer() method to print out all the elements of the array after the deletions; should be 3 4
        arr.add(9); //Adds 9 to the buffer array with the add() method
        arr.add(20); //Adds 20 to the buffer array with the add() method
        arr.add(5); //Adds 5 to the buffer array with the add() method
        arr.printBuffer(); //Invokes the printBuffer() method to print out all the elements of the array, should be 3 4 9 20 5
        arr.add(12039120); //Attempts to invoke the add() method to add the value 12039120 to the array. However, the array is full and we will be notified that we cannot add any more elements, as the array is full
    }
    //The time complexity of this program is 1 millisecond for this input. This runner program gas a Linear - O(n) - run time complexity in the worst case.
    //The space complexity of this program is 1.8 megabytes. This also has a space complexity of 4n + 4 ~ O(n), which is a LINEAR space complexity.
}
