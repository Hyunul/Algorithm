import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        // 신고 목록 체크
        Set<String> reports = new HashSet<>(Arrays.asList(report));
        
        // 신고 당한 횟수
        Map<String, Integer> reportCnt = new HashMap<>();
        for (String r : reports) {
            String[] part = r.split(" ");
            String to = part[1];
            
            reportCnt.put(to, reportCnt.getOrDefault(to, 0) + 1);
        }
        
        // 메일 받을 횟수
        Map<String, Integer> mailCnt = new HashMap<>();
        for (String r: reports) {
            String[] part = r.split(" ");
            String from = part[0];
            String to = part[1];
            
            if (reportCnt.getOrDefault(to, 0) >= k) {
                mailCnt.put(from, mailCnt.getOrDefault(from, 0) + 1);
            }
        }
        
        int[] answer = new int[id_list.length];
        
        for (int i = 0; i < id_list.length; i++) {
            answer[i] = mailCnt.getOrDefault(id_list[i], 0);
        }
        return answer;
    }
}