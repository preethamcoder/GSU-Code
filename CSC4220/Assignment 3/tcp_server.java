import java.io.*;
import java.net.*;

public class tcp_server {
    public static String reverse(String string){
        String res = "";
        for(int each = 0; each < string.length(); each++){
            res = string.charAt(each) + res;
        }
        return res;
    }
    public static void main(String[] args) throws IOException {
        int port = 8080;
        ServerSocket serverSocket = new ServerSocket(port);
        Socket clientSocket = serverSocket.accept();
        while (true) {
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            PrintWriter outer = new PrintWriter(clientSocket.getOutputStream(), true);
            String clientMessage = in.readLine();
            String modifiedMessage = reverse(clientMessage);
            outer.println(modifiedMessage);
            System.out.println("Modified message sent: " + modifiedMessage);
        }
        //clientSocket.close();
    }
}
