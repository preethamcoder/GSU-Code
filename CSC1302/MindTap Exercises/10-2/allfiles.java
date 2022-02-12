public class Candle
{
    int height;
    double price;
    private String color;

    public void setHeight(int h){
        height = h;
        price = 2.0 * h;
    }
    public void setColor(String col){
        color = col;
    }
    public double getPrice(){
        return price;
    }
    public int getHeight(){
        return height;
    }
    public String getColor(){
        return color;
    }
}

public class DemoCandles
{
   public static void main(String args[])
   {
      Candle aCandle = new Candle();
      ScentedCandle aScentedCandle = new ScentedCandle();
      aCandle.setColor("pink");
      aCandle.setHeight(6);
      aScentedCandle.setColor("white");
      aScentedCandle.setScent("gardenia");
      aScentedCandle.setHeight(6);
      System.out.println("The " + aCandle.getHeight() +
         " inch " + aCandle.getColor() +
         " candle costs $" + aCandle.getPrice());
      System.out.println("The " + aScentedCandle.getHeight() + " inch " +
         aScentedCandle.getScent() +
         " " + aScentedCandle.getColor() +
         " candle costs $" + aScentedCandle.getPrice());
   }
}

public class ScentedCandle extends Candle
{
    private String scent;

    public void setScent(String sce){
        scent = sce;
    }
    public String getScent(){
        return scent;
    }
    public void setHeight(int hei){
        super.height = hei;
        super.price = 3.0 * super.height;
    }
}
