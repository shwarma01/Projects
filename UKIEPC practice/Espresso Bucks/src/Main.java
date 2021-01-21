import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main main = new Main();
        int[] size = new int[2];
        String sizeStr = scanner.nextLine();
        char[][] grid = new char[0][];

        for (int i = 0; i < sizeStr.length(); i++) {
            if (sizeStr.charAt(i) == ' ') {
                size[0] = Integer.parseInt(sizeStr.substring(0, i));
                size[1] = Integer.parseInt(sizeStr.substring(i + 1));
                grid = new char[size[0]][size[1]];
                break;
            }
        }

        for (int row = 0; row < size[0]; row++) {
            grid[row] = scanner.nextLine().toCharArray();
        }

        System.out.println(main.toString(grid));
    }

    private String toString(char[][] grid) {
        StringBuilder returnStr = new StringBuilder();

        for (char[] chars : grid) {
            for (char aChar : chars) {
                returnStr.append(aChar);
            }
            returnStr.append("\n");
        }

        return returnStr.toString();
    }
}
