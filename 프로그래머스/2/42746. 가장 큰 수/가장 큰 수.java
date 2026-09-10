import java.util.Arrays;

class Solution {
    public String solution(int[] numbers) {
        String[] strNumbers = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            strNumbers[i] = String.valueOf(numbers[i]);
        }

        Arrays.sort(strNumbers, (s1, s2) -> (s2 + s1).compareTo(s1 + s2));

        if (strNumbers[0].equals("0")) {
            return "0";
        }

        StringBuilder sb = new StringBuilder();
        for (String str : strNumbers) {
            sb.append(str);
        }

        return sb.toString();
    }
}