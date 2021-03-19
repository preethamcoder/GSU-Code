public class GradeException extends Exception {
    public static char validGradeLetters[] = {'A', 'B', 'C', 'D', 'F', 'I'};
    public GradeException(String string) {
        super(string);
    }
}
