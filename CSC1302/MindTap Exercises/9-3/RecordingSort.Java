import java.util.*;
public class RecordingSort{
    public static void main(String[] args) {
       String title;
       String name;
       int time;
       Scanner scan=new Scanner(System.in);
        Recording[] Recordingobj = new Recording[5];
        for(int i=0;i<5;i++)
        {
            System.out.print("Enter Song Name: ");
            title=scan.nextLine();
            System.out.print("Enter Artist Name: ");
            name=scan.nextLine();
            System.out.print("Enter the duration: ");
            time=scan.nextInt();
            scan.nextLine();
            Recordingobj[i]=new Recording();
            Recordingobj[i].setSong(title);
            Recordingobj[i].setArtist(name);
            Recordingobj[i].setPlayTime(time);
        }
        sortByArtist(Recordingobj);      
        sortBySong(Recordingobj);      
        sortByTime(Recordingobj);
    }
  
    public static void sortByArtist(Recording[] array) {
       Arrays.sort(array, new Comparator<Recording>()) {
           @Override
           public int compare(Recording first, Recording second) {
               return first.getArtist().compareTo(second.getArtist());
           }
       });
       System.out.println("------Sort by Artist-----");
       for(int i=0;i<5;i++)
       {
            System.out.println("Title: "+array[i].getSong()+" Artist: "+array[i].getArtist()+" Time: "+array[i].getPlayTime()+"\n");
       }
    }
  
    public static void sortBySong(Recording[] array) {
           Arrays.sort(array, new Comparator<Recording>() {
               @Override
               public int compare(Recording first, Recording second) {
                   return first.getSong().compareTo(second.getSong());
               }
           });
           System.out.println("------Sort by Song-----");
           for(int i=0;i<5;i++)
           {
               System.out.println("Title: "+array[i].getSong()+" Artist: "+array[i].getArtist()+" Time: "+array[i].getPlayTime()+"\n");
           }
    }
  
    public static void sortByTime(Recording[] array) {
           Arrays.sort(array, new Comparator<Recording>() {
               @Override
               public int compare(Recording first, Recording second) {
                   return first.getPlayTime()-second.getPlayTime();
               }
           });
           System.out.println("------Sort by Time-----");
           for(int i=0;i<5;i++)
           {
               System.out.println("Title: "+array[i].getSong()+" Artist: "+array[i].getArtist()+" Time: "+array[i].getPlayTime()+"\n");
           }
    }
}
