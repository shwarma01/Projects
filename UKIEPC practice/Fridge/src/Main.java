import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean end = false;
        String dataIn = scanner.nextLine();
        int[] data = new int[] { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

        for (char c : dataIn.toCharArray()) {
            data[Integer.parseInt(String.valueOf(c))]++;
        }

        for (int i = 1; i <= Long.parseLong(dataIn); i++) {
            int[] dataCopy = data.clone();
            for (char n : String.valueOf(i).toCharArray()) {
                dataCopy[Integer.parseInt(String.valueOf(n))]--;

                if (dataCopy[Integer.parseInt(String.valueOf(n))] < 0) {
                    end = true;
                    break;
                }
            }

            if (end) {
                System.out.println(i);
                break;
            }
        }
    }
}
