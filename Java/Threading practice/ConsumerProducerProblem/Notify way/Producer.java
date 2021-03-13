public class Producer implements Runnable {

  private Shared data;

  public Producer(Shared data) {
    this.data = data;
  }

  @Override
  public void run() {
    while (true) {
      try {
        synchronized (data) {
          while (data.isFull()) {
            System.out.println("Data full");
            data.wait();
          }

          data.add();
          data.notify();
        }

        System.out.println("Data added");
        Thread.sleep(1000);
      } catch (InterruptedException e) {
        return;
      }
    }
  }
}
