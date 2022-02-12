public class ProductNode{
    String name;
    String locator;
    int quantity;
    float price;
    ProductNode next;
    
    public ProductNode(){ // default constructor
          quantity = 0;
          price = 0;
          name="";
          locator="";
          next = null;
    }

    public ProductNode(String name, String locator, int quantity, float price){ //Constructor that takes Parameters
          this.name = name;
          this.locator = locator;
          this.quantity = quantity;
          this.price = price;
          this.next = null;
    }
}
