public class InternationalDivision extends Division
{
    protected String country;
    protected String language;
    public InternationalDivision(String title, int acct, String cty, String lang)
    {
       super(title, acct);
       country = cty;
       language = lang;
    }
    public void display()
    {
        System.out.println(language + " " + country + " " + super.divisionTitle + " " + super.acctNum);
    }
}

