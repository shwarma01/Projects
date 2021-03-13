import java.util.ArrayList;

public class Shared {

  public ArrayList<Integer> data;
  private int max;

  public Shared(int max) {
    data = new ArrayList<Integer>();
    this.max = max;
  }

  public boolean isFull() {
    return max == data.size();
  }

  public boolean isEmpty() {
    return 0 == data.size();
  }

  public void add() {
    data.add(0);
  }

  public void remove() {
    data.remove(0);
  }
}
