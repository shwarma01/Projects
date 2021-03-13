public class Consumer implements Runnable {

  private Shared data;

  public Consumer(Shared data) {
    this.data = data;
  }

  @Override
  public void run() {
    while (true) {
      try {
        synchronized (data) {
          while (data.isEmpty()) {
            System.out.println("No data");
            data.wait();
          }

          data.remove();
          data.notify();
        }

        System.out.println("Data removed");
        Thread.sleep(1000);
      } catch (InterruptedException e) {
        return;
      }
    }
  }
}
