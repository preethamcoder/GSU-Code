import java.io.*;
import java.net.*;
import java.util.Scanner;

public class tcp_client {
    public static void main(String[] args) throws IOException {
        String serverAddress = "localhost";
        int serverPort = 8080;
        Socket socket = new Socket(serverAddress, serverPort);
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter outer = new PrintWriter(socket.getOutputStream(), true);
        Scanner scan = new Scanner(System.in);
        String message = "";
        while(!((message.toLowerCase()).equals("end"))){
        message = scan.nextLine();
        System.out.println("Sending message to server: " + message);
        outer.println(message);
        String modifiedMessage = in.readLine();
        System.out.println("Received modified message from server: " + modifiedMessage);
        }
        scan.close();
        socket.close();
    }
}
