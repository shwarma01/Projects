import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int limit = s.nextLine().length();
        if (limit >= s.nextLine().length()) {
            System.out.println("go");
        }
        else{
            System.out.println("no");
        }
    }
}