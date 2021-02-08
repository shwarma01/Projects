import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;


public class Client {
  private Socket serverSocket;

  public Client(String address) {
    try {
      serverSocket = new Socket(address, 14003);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  public void run() {
    System.out.println("Client Started");

    try {
      String lastUserInput = "";
      BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));

      PrintWriter serverOut = new PrintWriter(serverSocket.getOutputStream(), true);

      BufferedReader serverIn = new BufferedReader(new InputStreamReader(serverSocket.getInputStream()));

      while (!lastUserInput.equals("exit")) {
        lastUserInput = userInput.readLine();
        serverOut.println(lastUserInput);
        System.out.println(serverIn.readLine());
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
    Client client = new Client("localhost");
    client.run();
  }
}
