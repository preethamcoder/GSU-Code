public class ProductInventory {
    ProductNode inventoryHead = new ProductNode(); //Intializes an inventory head for the LinkedList
    int totalProduct = 0; //Counts the total number of products - only for debugging purposes
    public void showInventory(){ //Prints the inventory 
        if (inventoryHead.next != null){
            System.out.printf("\n%50s%20s%15s%15s", "Product Name", "Locator", "Quantity", "Price"); //Assuming the formating of output doesn't matter
            System.out.println("\n---------------------------------------------------------------------------------------------------------");
            ProductNode curr = inventoryHead.next; 
            while (curr != null){ //Prints every node in the list
                System.out.printf("%50s%20s%15d%15.2f\n", curr.name, curr.locator, curr.quantity, curr.price);
                curr = curr.next;
            }
        }else{
            throw new ProductException("Empty Inventory"); //Throws new product exception if the inventory is Empty
        }
    }
    public int getTotalQuantity(){ //Displays the total quanitity of available products in the inventory
        int totalQuantity = 0;
        if (inventoryHead.next != null){
            ProductNode curr = inventoryHead.next; //Temp variable
            while (curr != null){ //Iterates through every node in the variable to add the total quantity
                totalQuantity += curr.quantity;
                curr = curr.next;
            }
        }
        return totalQuantity; //Returns the total quanitiy
    }
    public ProductNode removeMaximum(){ //Removes the largest value node present in the inventory
        ProductNode maxNode = null; //Variable to store the node with the maximum quantity
        ProductNode maxNodeLast = null; //Variable to store the previous node of maximum quantity
        if (inventoryHead.next != null){ //Iterates till the end of the list
            ProductNode curr = inventoryHead.next; 
            ProductNode prev = inventoryHead;
            maxNodeLast = prev; 
            maxNode = curr; //Assings variables to store the largest value node
            while (curr != null){ //Iterates through the whole list
                if (maxNode.quantity < curr.quantity){ //Finds the node with maximum quantity
                    maxNode = curr; //Saves the node
                    maxNodeLast = prev; //Saves the previous node as well
                }
                prev = curr; //Iterator
                curr = curr.next; //Iterator
            }
            maxNodeLast.next = maxNode.next; //Iterator
            totalProduct--; //Only for debugging
        }
        return maxNode; //Returns the maximum node
    }
    public void sortInventory(){ //Sorts the inventory with the maximum quantity first and minimum quantity node last
        if (inventoryHead.next != null){ 
            ProductInventory sortInventoryNode = new ProductInventory(); //Temp variable
            while (inventoryHead.next != null){ //Iterates the List
                ProductNode maxNode = removeMaximum(); //Finds the maximum quanity node and removes it
                sortInventoryNode.addProduct(maxNode.name, maxNode.locator, maxNode.quantity, maxNode.price); //Adds it to the front of the list
            }
            inventoryHead.next = sortInventoryNode.inventoryHead.next; //Iterator
        }
    }
    public void addProduct(String productName, String locator, int quantity, float price) { //Adds a product to the List
        ProductNode node = new ProductNode(productName, locator, quantity, price); //Creates a new node in the list
        if (inventoryHead == null){  //Assigns the node to the inventory head if it is the first node
            inventoryHead = node;
        }
        else {
            ProductNode last = inventoryHead; //Intializes inventory head to last
            while (last.next != null) {
                last = last.next;
            }
            last.next = node;
        }
    }
    public void removeProduct(String productName, String locator){ //Removes a product
        if (inventoryHead.next != null){ //Iterates till the end of the list
            ProductNode curr = inventoryHead.next; //Assigns temp variable
            ProductNode prev = inventoryHead; //Assigns temp variable
            while (curr != null){ //Iterates through the list 
                if (curr.name.equalsIgnoreCase(productName) && curr.locator.equalsIgnoreCase(locator)){ //Finds the Product to remove
                    if (prev == inventoryHead){ 
                        inventoryHead.next = curr.next; //Removes the Product
                    }else {
                       prev.next = curr.next;
                    }
                    break;
                }
                prev = curr;
                curr = curr.next;
            }
            totalProduct--; //Only for debugging
        }
    }
    public int countNeededQuantity(String productName, int neededQuantity){ //Calculates the Quantity Needed by Subtracting the passed value and the current value
        int quant = countTotalQuant(productName); //Calls the Count Total Quant method
        if (quant < neededQuantity) 
            return (neededQuantity - quant); //Returns the number needed more  
        return 0; //Returns if the needed quanity is less than actual one
    }
    public int countTotalQuant(String productName){ //Counts the Total Quantity at Hand
        int totalQuantity = 0; 
        if (inventoryHead.next != null){
            ProductNode curr = inventoryHead.next;
            while (curr != null){ //Iterates to the list
                if (curr.name.equalsIgnoreCase(productName)){
                    totalQuantity += curr.quantity; //Collects the quantity for the pointed node
                }
                curr = curr.next;
            }
        }
        return totalQuantity; //Returns the total Quantity on Hand
    }
    class ProductException extends RuntimeException { //Product Exception Method to Handle and debug errors
        public ProductException(String s){
            super(s);
        }
    }
}