public class Fiction extends Book
{
    public Fiction(String s){
        super(s);
        setPrice();
    }
  
    public void setPrice(){
        super.price = 24.99;
        System.out.println(super.price);
    }
    public String getTitle(){
        return(super.title);
    }

}
