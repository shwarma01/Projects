import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;

public class Server {
  private ServerSocket serverSocket;
  private String[] replies;
  private Random random;

  public Server() {
    try {
      serverSocket = new ServerSocket(14003);
    } catch (IOException e) {
      e.printStackTrace();
    }

    replies = new String[] {
      "As I see it, yes.",
      "Ask again later.",
      "Better not tell you now.",
      "Cannot predict now.",
      "Concentrate and ask again.",
      "Don’t count on it.",
      "It is certain.",
      "It is decidedly so.",
      "Most likely.",
      "My reply is no.",
      "My sources say no.",
      "Outlook not so good.",
      "Outlook good.",
      "Reply hazy, try again.",
      "Signs point to yes.",
      "Very doubtful.",
      "Without a doubt.",
      "Yes.",
      "Yes – definitely.",
      "You may rely on it."
    };

    random = new Random();
  }

  public void run() {
    System.out.println("Server listening");

    try {
      Socket clientSocket = serverSocket.accept();
      System.out.println("Server accepted connection");

      String clientInput = "";
      BufferedReader clientIn = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

      PrintWriter clientOut = new PrintWriter(clientSocket.getOutputStream(), true);

      while (!clientInput.equals("exit")) {
        clientInput = clientIn.readLine();

        if (clientInput.equals("exit")) {
          clientOut.println("See ya later!");
        } else {
          clientOut.println(replies[random.nextInt(replies.length)]);
        }
      }
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      try {
        serverSocket.close();
      } catch (Exception e) {
        e.printStackTrace();
      }
    }
  }

  public static void main(String[] args) {
    Server server = new Server();
    server.run();
  }
}