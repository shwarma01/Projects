public class Main {

  public static void main(String[] args) {
    boolean[] chopsticks = new boolean[5];
    Thread[] threads = new Thread[chopsticks.length];
    for (int i = 0; i < chopsticks.length; i++) {
      chopsticks[i] = true;
      threads[i] =
        new Thread(new Philosopher(i, chopsticks));
      threads[i].start();
    }

    try {
      Thread.sleep(5000);

      for (int i = 0; i < 2; i++) {
        for (Thread thread : threads) {
          if (i == 0) thread.interrupt(); else thread.join();
        }
      }

      System.out.println("Everyone has left");
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
  }
}
