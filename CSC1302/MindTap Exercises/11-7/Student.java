public abstract class Student
{
    String id;
    String lastName;
    double tuition;
    public Student(String id, String name)
    {
        this.id = id;
        lastName = name;
    }
    public void setId(String idNum)
    {
        id = idNum;
    }
    public void setLastName(String name)
    {
        lastName = name;
    }
    public String getId()
    {
        return(id);
    }
    public String getLastName()
    {
        return(lastName);
    }
    public double getTuition()
    {
        return(tuition);
    }
    public abstract void setTuition();
}
