import java.util.*;

class Solution {
    public int solution(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        int maxPick = nums.length / 2; // n/2 마리 get
        return Math.min(set.size(), maxPick);
    }
}