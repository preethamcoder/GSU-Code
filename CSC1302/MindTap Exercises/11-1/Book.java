public abstract class Book
{
   String title = "";
   double price = 0.0;
   public Book(String head){
       title = head;
   }
   public abstract void setPrice();
   public String getTitle(){
       return(title);
   }
   public double getPrice(){
       return(price);
   }
}
