public class Philosopher implements Runnable {

  private boolean[] chopsticks;
  private int id;

  public Philosopher(int id, boolean[] chopsticks) {
    this.chopsticks = chopsticks;
    this.id = id;
  }

  private boolean canEat() {
    return chopsticks[id] == chopsticks[(id + 1) % chopsticks.length];
  }

  private void eating() {
    chopsticks[id] = false;
    chopsticks[(id + 1) % chopsticks.length] = false;
  }

  private void thinking() {
    chopsticks[id] = true;
    chopsticks[(id + 1) % chopsticks.length] = true;
  }

  @Override
  public void run() {
    try {
      while (true) {
        synchronized (chopsticks) {
          System.out.println("Philosopher " + (id + 1) + " wants to eat");
          while (!canEat()) {
            chopsticks.wait();
          }

          eating();
          System.out.println("Philosopher " + (id + 1) + " has started eating");
        }
        Thread.sleep(1000);

        synchronized (chopsticks) {
          thinking();
          System.out.println(
            "Philosopher " + (id + 1) + " has finished eating and is thinking"
          );
          chopsticks.notifyAll();
        }
        Thread.sleep(1000);
      }
    } catch (InterruptedException e) {
      System.out.println("Philosopher " + (id + 1) + " has payed and left");
      return;
    }
  }
}
