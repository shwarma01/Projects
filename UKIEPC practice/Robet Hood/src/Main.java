import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int C = Integer.parseInt(scanner.nextLine());
        long[][] coords = new long[C][2];
        long result = (long) 0.0;

        for (int c = 0; c < C; c++) {
            String data = scanner.nextLine();
            for (int i = 0; i < data.length(); i++) {
                if (data.charAt(i) == ' ') {
                    coords[c][0] = Long.parseLong(data.substring(0, i));
                    coords[c][1] = Long.parseLong(data.substring(i + 1));
                    break;
                }
            }
        }

        for (int i = 0; i < coords.length - 1; i++) {
            for (int j = i + 1; j < coords.length; j++) {
                long tempResult = (long) (Math.pow(coords[i][0], 2) + Math.pow(coords[i][1], 2) + Math.sqrt(Math.pow(coords[j][0], 2) + Math.pow(coords[j][1], 2)));

                long angle = (coords[i][0] * coords[j][0]) + (coords[i][1] * coords[j][1]);
                long dotProduct = (long) Math.sqrt(Math.pow(coords[i][0], 2) + Math.pow(coords[i][1], 2));
                dotProduct *= (long) Math.sqrt(Math.pow(coords[j][0], 2) + Math.pow(coords[j][1], 2));
                angle /= dotProduct;

                tempResult -= 2 * Math.sqrt(Math.pow(coords[i][0], 2) + Math.pow(coords[i][1], 2)) * Math.sqrt(Math.pow(coords[j][0], 2) + Math.pow(coords[j][1], 2)) * angle;
                result = Math.max(tempResult, result);
            }
        }

        System.out.println(Math.sqrt(result));
    }
}
