import java.nio.file.*;
import java.io.FileWriter;
import static java.nio.file.AccessMode.*;
import java.io.*;
import java.nio.channels.FileChannel;
import java.nio.ByteBuffer;
import static java.nio.file.StandardOpenOption.*;
public class ValidateCheckDigits {
    public static void main(String[] args) {
        Path fileIn = Paths.get("/root/sandbox/AcctNumsIn.txt");
        Path fileOut = Paths.get("/root/sandbox/AcctNumsOut.txt");
        //InputStream input = null;
        //String s = "a";
       try{
        InputStream input = new BufferedInputStream(Files.newInputStream(fileIn));
        BufferedReader reader = new BufferedReader(new InputStreamReader(input));
        OutputStream output = new BufferedOutputStream(Files.newOutputStream(fileOut));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(output));
        String s = "1";
        while(s != null){
            s = reader.readLine();
            if(s != null){
                System.out.println(s);
                int a = Integer.parseInt(s.substring(0,1));
                int b = Integer.parseInt(s.substring(1,2));
                int c = Integer.parseInt(s.substring(2,3));
                int d = Integer.parseInt(s.substring(3,4));
                int e = Integer.parseInt(s.substring(4,5));
                int f = Integer.parseInt(s.substring(5,6));
                if(((a+b+c+d+e) % 10) == f){
                  s += "\n";
                  writer.write(s, 0, s.length());
            }
            }
        }
        
        //int sd = 0;
        //System.out.println(s);
        //}
    reader.close();
    writer.close();
       
       }catch(IOException exc){
           System.out.println(exc);
       }
        
    }
}

