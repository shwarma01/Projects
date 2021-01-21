import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int bombs = scanner.nextInt() - 2;

        if (bombs <= 0) {
            System.out.println(1);
        }
        else {
            System.out.println(bombs);
        }
    }
}
