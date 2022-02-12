public class Course {
    String department;
    int courseNumber;
    double credits;
    final int DEPT_LENGTH = 3;
    final int LOW_NUM = 100;
    final int HIGH_NUM = 499;
    final double LOW_CREDITS = 0.5;
    final double HIGH_CREDITS = 6;
    public Course() {
        department = "";
        courseNumber = 0;
        credits = 0.0;
    }
    public Course(String dept, int num, double creditValue) throws CourseException {
        String msg = "";
        department = dept;
        credits = creditValue;
        courseNumber = num;
        if(dept.length()!=DEPT_LENGTH){
            msg += "Department should be atleast 3 characters";
        }if(credits < LOW_CREDITS || credits > HIGH_CREDITS){
            msg += "Invalid credits";
        }
        if(courseNumber < 100 || courseNumber >= 500){
            msg += "Invalid course #";
        }
        if(msg.length() > 0){
            throw(new CourseException(msg + "\n" + department + courseNumber + credits));
        }
        }
        
    public String toString() {
        //System.out.println(department + " " + courseNumber + " " + credits);
        return(department + " " + courseNumber + " " + credits);
    }
}
