import javax.lang.model.util.ElementScanner14;

public class Triangle2 {
    public static void triangle_0_1(int n) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                if ((i + j) % 2 == 0) {
                    System.out.print("1 ");
                }
                System.out.print("0 ");
            }
            System.out.println();
        }
    }

    public static void main(String args[]) {
        triangle_0_1(5);

    }
}
