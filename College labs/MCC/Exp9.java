class Exp9 {
   
    public static String a3Algorithm(String key, String rand) {
        int[] k = hexStringToIntArray(key);
        int[] r = hexStringToIntArray(rand);
        
        int[] op = new int[8];
        for (int i = 0; i < 8; i++) {
            op[i] = k[i] ^ r[i];
        }

        String result = intArrayToHexString(op);
        return result;
    }
    
    public static int[] hexStringToIntArray(String hexString) {
        int[] result = new int[hexString.length() / 2];
        for (int i = 0; i < hexString.length(); i += 2) {
            result[i / 2] = Integer.parseInt(hexString.substring(i, i + 2), 16);
        }
        return result;
    }

    public static String intArrayToHexString(int[] intArray) {
        StringBuilder sb = new StringBuilder();
        for (int i : intArray) {
            sb.append(String.format("%02X", i));
        }
        return sb.toString();
    }
    public static void main(String[] args) {
        
        String key = "133457799BBCDFF1";
        String rand = "1234567890ABCDEFFEDCBA0987654321";
        String expectedRes = "B3DC1BFE642DADBC";
    
        String res = a3Algorithm(key, rand);
        System.out.println("\n128 Bit Key: " + key);
        System.out.println("128 Random Bits Generated: " + rand);
        System.out.println("\nExpected Result: " + expectedRes);
        System.out.println("Result: " + res);
        System.out.println("\nMatch: " + res.equals(expectedRes));
        System.out.println();
    }
}
