public class DecimalToBinary {
    public static void decToBin(int n) {
        int pow = 0, binNo = 0;
        int Myno = n;
        while (n > 0) {
            int rem = n % 2;
            binNo = binNo + (rem * (int) Math.pow(10, pow));
            pow++;
            n = n / 2;

        }
        System.out.println("Binary of" + Myno + "=" + binNo);
    }

    public static void main(String args[]) {
        decToBin(5);
    }

}
