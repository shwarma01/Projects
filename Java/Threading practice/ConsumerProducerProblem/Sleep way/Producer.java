public class Producer implements Runnable {

  private Shared data;

  public Producer(Shared data) {
    this.data = data;
  }

  @Override
  public void run() {
    for (int i = 0; i < 10; i += 2) {
      if (!data.isFull()) {
        data.add();
        System.out.println("Data added");
      }

      try {
        Thread.sleep(100);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }
}
