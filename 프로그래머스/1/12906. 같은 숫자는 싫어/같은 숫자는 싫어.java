import java.util.*;

public class Solution {
    public ArrayList<Integer> solution(int[] arr) {
    ArrayList<Integer> answer = new ArrayList<>();
        int prev = -1;
        for (int num : arr) {
            if (prev == num) {
                continue;
            }
            else {
                answer.add(num);
            }
            prev = num;
        }
        
        return answer;
    }
}