public class DomesticDivision extends Division
{
    protected String state;
    public DomesticDivision(String title, int acct, String st)
    {
        super(title, acct);
        state = st;
    }
    public void display()
    {
        System.out.println(super.divisionTitle + " " + state + " " + super.acctNum);
    }
}

