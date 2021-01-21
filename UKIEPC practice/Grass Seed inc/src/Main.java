import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double result = 0;
        double cost = Double.parseDouble(scanner.nextLine());
        int lawns = Integer.parseInt(scanner.nextLine());
        double[][] sizes = new double[lawns][2];

        for (int l = 0; l < lawns; l++) {
            String sizeStr = scanner.nextLine();
            for (int i = 0; i < sizeStr.length(); i++) {
                if (sizeStr.charAt(i) == ' ') {
                    sizes[l][0] = Double.parseDouble(sizeStr.substring(0, i));
                    sizes[l][1] = Double.parseDouble(sizeStr.substring(i + 1));
                    break;
                }
            }
        }

        for (double[] size : sizes) {
            result += size[0] * size[1] * cost;
        }

        System.out.println(String.format("%.7f", result));
    }
}
