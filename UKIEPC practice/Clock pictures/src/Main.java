import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[][] info = new int[2][Integer.parseInt(scanner.nextLine())];
        for (int i = 0; i < 2; i++) {
            String data = scanner.nextLine() + ' ';
            int counter = 0;
            int offset = 0;
            for (int j = 0; j < data.length(); j++) {
                if (data.charAt(j) == ' ') {
                    info[i][counter] = Integer.parseInt(data.substring(offset, j));
                    offset = j + 1;
                    counter++;
                }
            }
        }

        boolean possible = true;
        for (int j = 0; j < info[0].length - 1; j++) {
            if (Math.abs(info[0][j] - info[0][j + 1]) != Math.abs(info[1][j] - info[1][j + 1])) {
                if (360000 - Math.abs(info[0][j] - info[0][j + 1]) != Math.abs(info[1][j] - info[1][j + 1])) {
                    possible = false;
                    break;
                }
            }
        }

        if (possible) { System.out.println("possible"); }
        else { System.out.println("impossible"); }
    }
}
