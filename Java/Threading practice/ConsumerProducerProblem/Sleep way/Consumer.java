public class Consumer implements Runnable {

  private Shared data;

  public Consumer(Shared data) {
    this.data = data;
  }

  @Override
  public void run() {
    for (int i = 1; i < 10; i += 2) {
      if (!data.isEmpty()) {
        data.remove();
        System.out.println("Data removed");
      }

      try {
        Thread.sleep(500);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }
}
