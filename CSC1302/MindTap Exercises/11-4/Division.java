public abstract class Division
{
    protected String divisionTitle;
    protected int acctNum;
    public Division(String title, int acct)
    {
        acctNum = acct;
        divisionTitle = title;
    }
    public abstract void display();
}

