import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Scheduler {

  private String[][] eventsInfo;
  private String[][] roomsInfo;
  private String[][] scheduled;
  private double[] times;

  public Scheduler(String filename) {
    try {
      BufferedReader bf = new BufferedReader(new FileReader(filename));
      String[] fileInfo = bf.readLine().split(" ");
      eventsInfo = new String[Integer.parseInt(fileInfo[0])][3];
      roomsInfo = new String[Integer.parseInt(fileInfo[1])][2];
      scheduled = new String[roomsInfo.length][eventsInfo.length];
      times =
        new double[] { Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY };
      int eventsCount = 0;
      int roomsCount = 0;

      String[] line;
      while (true) {
        line = bf.readLine().split(" ");
        if (line.length == 4) {
          eventsInfo[eventsCount] = line;
          times[0] = Math.min(times[0], Double.parseDouble(line[1]));
          times[1] = Math.max(times[1], Double.parseDouble(line[2]));
          eventsCount++;
        } else {
          roomsInfo[roomsCount] = line;
          scheduled[roomsCount][0] = line[0];
          roomsCount++;
        }

        if (roomsCount + 1 == roomsInfo.length) {
          break;
        }
      }

      bf.close();
    } catch (FileNotFoundException e) {
      System.out.println("File not found");
    } catch (IOException e) {
      System.out.println("Couldn't read file");
    }
  }

  public void schedule() {}

  public void printToFile() {
    File file = new File("output.txt");
    try {
      file.createNewFile();
      FileWriter fileWriter = new FileWriter("output.txt");

      for (String[] info : scheduled) {
        fileWriter.write(arrayToString(info));
      }

      fileWriter.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  private String arrayToString(String[] array) {
    String string = array[0] + ": ";

    for (int i = 1; i < array.length; i++) {
      string += array[i] + " ";
    }

    return string.substring(0, string.length() - 1) + "\n";
  }

  public static void main(String[] args) {
    Scheduler scheduler = new Scheduler("data_5000_3.in");
    scheduler.schedule();
    // scheduler.printToFile();
  }
}
