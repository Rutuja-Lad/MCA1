class HollowRect {
    static void rectangle(int rows, int cols) {
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                if (i == 1 || i == rows || j == 1 || j == cols) {
                    System.out.println("*");
                } else {
                    System.out.println(" ");
                }

            }
        }
    }

    public static void main(String args[]) {
        rectangle(5, 7);
    }
}