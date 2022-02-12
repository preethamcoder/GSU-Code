public class Rock
{
    private int sampleNumber;
    private String description;
    private double weight;

    public Rock(int samno, double w8){
        sampleNumber = samno;
        weight = w8;
        description = "Unclassified";
    }
    public int getSampleNumber(){
        return sampleNumber;
    }
    public void setDescription(String descf){
        description = descf;
    }
    public String getDescription(){
        return description;
    }
    public double getWeight(){
        return weight;
    }
}

public class SedimentaryRock extends Rock
{
   public SedimentaryRock(int smno, double weig){
       super(smno, weig);
       super.setDescription("Sedi");
   }
}

public class MetamorphicRock extends Rock
{
   public MetamorphicRock(int smno, double weig){
       super(smno, weig);
       super.setDescription("Meta");
   }
}

public class IgneousRock extends Rock
{
   public IgneousRock(int smno, double weig){
       super(smno, weig);
       super.setDescription("Igenous");
   }
}

import java.util.*;
public class DemoRocks
{
   public static void main(String[] args)
   {
      // Write the demo program here
   }
}
