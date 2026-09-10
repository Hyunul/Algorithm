import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[] array, int[][] commands) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int[] command : commands) {
            int[] temp_arr = Arrays.copyOfRange(array, command[0]-1, command[1]);
            Arrays.sort(temp_arr);
            answer.add(temp_arr[command[2]-1]);
        }
        
        return answer;
    }
}