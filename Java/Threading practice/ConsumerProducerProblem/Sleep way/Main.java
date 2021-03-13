public class Main {

  public static void main(String[] args) {
    Shared data = new Shared(10);
    Thread producer = new Thread(new Producer(data));
    Thread consumer = new Thread(new Consumer(data));
    producer.start();
    consumer.start();
  }
}
