public class NonFiction extends Book
{
    public NonFiction(String s){
        super(s);
        setPrice();
    }
  
    public void setPrice(){
        super.price = 37.99;
        //System.out.println(super.price);
    }
    public String getTitle(){
        return(super.title);
}
}
