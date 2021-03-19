import java.util.*;
public class Faculty extends CollegeEmployee
{
    private boolean isTenured = false;
    Scanner input = new Scanner(System.in);
    @Override
        public void setData()
        {
            super.setData();
            isTenured = input.nextBoolean();
        }
    @Override
        public void display()
        {
            super.display();
            if(isTenured){
                System.out.println("Faculty member is tenured");
            }else{
                System.out.println("Faculty member is not tenured");
            }
        }
}
