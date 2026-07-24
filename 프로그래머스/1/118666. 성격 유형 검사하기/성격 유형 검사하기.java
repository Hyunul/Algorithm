import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        Map<Character, Integer> score = new HashMap<>();
        
        // 각 유형 cnt 초기화
        for (char type : "RTCFJMAN".toCharArray()) {
            score.put(type, 0);
        }
        
        for (int i = 0; i < survey.length; i++) {
            char first = survey[i].charAt(0); // 첫번째 유형 (동의)
            char second = survey[i].charAt(1); // 두번째 유형 (비동의)
            int choice = choices[i];
            
            // 4(모르겠음)으로부터의 거리 계산
            if (choice < 4) {
                score.put(first, score.get(first) + 4 - choice);
            } else if (choice > 4) {
                score.put(second, score.get(second) + choice - 4);
            }
        }
        
        StringBuilder answer = new StringBuilder();
        
        answer.append(score.get('R') >= score.get('T') ? 'R': 'T');
        answer.append(score.get('C') >= score.get('F') ? 'C': 'F');
        answer.append(score.get('J') >= score.get('M') ? 'J': 'M');
        answer.append(score.get('A') >= score.get('N') ? 'A': 'N');
        
        return answer.toString();
    }
}