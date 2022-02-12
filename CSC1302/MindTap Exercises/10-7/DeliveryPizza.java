public class DeliveryPizza extends Pizza{
   double deliveryFee = 0.0;
   String address = "";

   public DeliveryPizza(String desc, double cost, String ad){
       super(desc, cost);
       address = ad;
       if(price > 15.00){
           deliveryFee = 3.0;
       }else{
           deliveryFee = 5.0;
       }
   }
}
