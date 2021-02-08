import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class EchoServer {
  private ServerSocket mySocket;

  public EchoServer() {
    try {
		  mySocket = new ServerSocket(14002); // Need address and port but address is already handled, use ports 1500+ (since below they may be being used for other stuff)
    } catch (IOException e) {
      e.printStackTrace();
    } 
  }

  public void go() {
    System.out.println("Server listening...");

    try {
      // Accept connection from client
      Socket clientSocket = mySocket.accept(); // Blocking, program cannot go further until a client connects
      System.out.println("Server accepted connection on: " + mySocket.getLocalPort() + "; " + clientSocket.getPort());

      // Ability to read from client
      BufferedReader clientIn = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

      // Ability to send data to client
      PrintWriter clientOut = new PrintWriter(clientSocket.getOutputStream(), true);

      // Read from client and send to client
      while(true) {
        String userInput = clientIn.readLine();
        clientOut.println(userInput);
      }
    } catch (IOException e) { 
      e.printStackTrace();
    } finally {
      try {
        mySocket.close();
      } catch (IOException e) {
        e.printStackTrace();
      }
    }
    
  }
  public static void main(String[] args) {
    EchoServer myEchoServer = new EchoServer();
    myEchoServer.go();
  }
}