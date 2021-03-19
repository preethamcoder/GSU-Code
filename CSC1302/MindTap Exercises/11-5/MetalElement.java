public class MetalElement extends Element
{
    public MetalElement(String s, int an, double aw)
    {
        super(s, an, aw);
    }
    public void describeElement()
    {
        System.out.println(super.symbol + " " + super.atomicNumber + " " + super.atomicWeight);
    }
}
