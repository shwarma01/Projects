public class Main {

  public static void main(String[] args) {
    Shared data = new Shared(5);
    Thread producer = new Thread(new Producer(data));
    Thread consumer = new Thread(new Consumer(data));

    producer.start();
    consumer.start();

    try {
      Thread.sleep(10000);
      System.out.println("Done waiting");

      producer.interrupt();
      consumer.interrupt();

      producer.join();
      consumer.join();
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
  }
}
