public class BinaryToDecimal {
    public static void binTodec(int binNum) {
        
        int pow = 0, decNum = 0;
        int Mynum = binNum;
        while (binNum > 0) {
            int lastDigit = binNum % 10;
            decNum = decNum + (lastDigit * (int) Math.pow(2, pow));
            pow++;
            binNum = binNum / 10;
        }
        System.out.println("Decimal of" + Mynum + "=" + decNum);
    }

    public static void main(String args[]) {
        binTodec(111);
    }
}
