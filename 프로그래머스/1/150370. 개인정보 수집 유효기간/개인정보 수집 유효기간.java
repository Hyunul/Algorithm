import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        int today_ilsu = exchange_ilsu(today); // 년월일을 일로 치환
        
        Map<String, Integer> term_ilsu = new HashMap<>();
        for (String term : terms) {
            String[] term_arr = term.split(" ");
            String term_kind = term_arr[0];
            int term_range = Integer.parseInt(term_arr[1]) * 28;
            
            term_ilsu.put(term_kind, term_range);
        }
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < privacies.length; i++) {
            String[] privacy = privacies[i].split(" ");
            int privacy_ilsu = exchange_ilsu(privacy[0]);
            int kind_ilsu = term_ilsu.get(privacy[1]);
            
            if (today_ilsu >= privacy_ilsu + kind_ilsu) {
                result.add(i+1);
            }
        }
        int[] answer = new int[result.size()];

        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        
        return answer;
    }
    
    private int exchange_ilsu(String entire_date) {
        String[] date_arr = entire_date.split("\\.");
        int total_ilsu = Integer.parseInt(date_arr[0]) * 12 * 28 + Integer.parseInt(date_arr[1]) * 28 + Integer.parseInt(date_arr[2]);
        
        return total_ilsu;
    }
}