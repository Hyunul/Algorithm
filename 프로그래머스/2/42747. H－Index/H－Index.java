import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int max = Arrays.stream(citations).max().getAsInt();
        for (int i = 0; i < max; i++ ) {
            int cnt = 0;
            for (int citation : citations) {
                if (citation >= i) {
                    cnt += 1;
                }
            }
            if (cnt < i) break;
            answer = i;
        }
        return answer;
    }
}