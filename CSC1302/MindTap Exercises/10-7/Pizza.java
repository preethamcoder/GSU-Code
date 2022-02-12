public class Pizza
{
   // Define the Pizza class here
   double price = 0.0;
   String description = "";

   public Pizza(String desc, double cost){
       price = cost;
       description = desc;
   }
   public void display(){
       String x = description + " pizza   Price: $" + price;
       System.out.println(x);
   }
}
