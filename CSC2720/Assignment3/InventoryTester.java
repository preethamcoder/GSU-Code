public class InventoryTester { //Runs the Inventory Class
       public static void main(String[] args)
       {
             ProductInventory inventory = new ProductInventory();
      
             inventory.addProduct("Apple iphone 7 plus 32gb rose gold", "box256", 10, 699.80f); //Add products to inventory
             inventory.addProduct("Apple iphone 7 plus 32gb rose gold", "shelf4", 4, 699.80f);//Add products to inventory
             inventory.addProduct("Apple macbook pro", "box15", 2, 1500.87f); //Add product to inventory
             inventory.addProduct("Dell monitor", "shelf10", 12, 221.54f); //Add product to inventory
       
             inventory.showInventory(); //Display inventory
             /*
             Product Name	Locator	Quantity	Price
             --------------------------------------------------------------------------
             Apple iphone 7 plus 32gb rose gold	box256	10	699.80
             Apple iphone 7 plus 32gb rose gold	shelf4	4	699.80
             Apple macbook pro	box14	2	1500.87
             Dell Monitor	shelf10	12	221.54
             */						
             inventory.sortInventory(); // Sorts products in inventory
             inventory.showInventory(); // Displays inventory
             /*						
             Product Name	Locator	Quantity	Price
             --------------------------------------------------------------------------
             Dell Monitor	shelf10	12	221.54
             Apple iphone 7 plus 32gb rose gold	box256	10	699.80
             Apple iphone 7 plus 32gb rose gold	shelf4	4	699.80
             Apple macbook pro	box14	2	1500.87
             */						
             System.out.println(inventory.countTotalQuant("Apple iphone 7 plus 32gb rose gold")); //Should return 14
             System.out.println(inventory.countNeededQuantity("Dell Monitor",15)); //Should return 3
             inventory.removeMaximum(); //Removes Product with Maximum Quantity
             inventory.removeProduct("Apple iphone 7 plus 32gb rose gold", "shelf4"); //Removes the Product
             System.out.println(inventory.getTotalQuantity()); //Should return 15
       }
}