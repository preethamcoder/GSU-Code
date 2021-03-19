import java.nio.file.*;
import java.nio.file.attribute.*;
import java.io.IOException;
import java.nio.channels.FileChannel;
public class FileSizeComparison {
    public static void main(String[] args) {
        Path textFile = Paths.get("/root/sandbox/lyric1.txt");
        Path wordFile = Paths.get("/root/sandbox/lyric2.txt");
        FileChannel fc;
        try{
            fc = FileChannel.open(textFile);
            long filesize = fc.size();
            System.out.println(filesize + " bytes");
        }catch(IOException exc){
            exc.printStackTrace();
        }
        try{
            fc = FileChannel.open(wordFile);
            long filesize = fc.size();
            System.out.println(filesize + " bytes");
        }catch(IOException exc){
            exc.printStackTrace();
        }
        try{
            fc = FileChannel.open(wordFile);
            long filesize1 = fc.size();
            FileChannel fc2 = FileChannel.open(textFile);
            double fs2 = fc2.size();
            double a = (100*fs2/filesize1);
            System.out.println(a + "%");
        }catch(IOException exc){
            exc.printStackTrace();
        }
    }
}
