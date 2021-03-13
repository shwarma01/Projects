import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class EchoClient {
  private Socket serverSocket;

  public EchoClient(String address) {
    try {
      serverSocket = new Socket(address, 14003);
    } catch (UnknownHostException e) {
      e.printStackTrace();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  public void go() {
    try {
      System.out.println("Client running...");
      
      // Ability to read user input from keyboard
      BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));

      // Ability to send data to server
      PrintWriter serverOut = new PrintWriter(serverSocket.getOutputStream(), true);

      // Ability to read data from server
      BufferedReader serverIn = new BufferedReader(new InputStreamReader(serverSocket.getInputStream()));

      while (true) {
        String userInputString = userInput.readLine();
        serverOut.println(userInputString);
        String serverResponse = serverIn.readLine();
        System.out.println(serverResponse);
      }
    } catch (IOException e) {
      e.printStackTrace();
    } finally {
      try {
        serverSocket.close();
      } catch (IOException e) {
        e.printStackTrace();
      }
    }
  }

  public static void main(String[] args) {
    EchoClient myEchoClient = new EchoClient("localhost");
    myEchoClient.go();
  }
}
