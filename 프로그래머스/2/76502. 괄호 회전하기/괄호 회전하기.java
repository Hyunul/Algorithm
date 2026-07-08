import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        int n = s.length();
        
        for (int i = 0; i < n; i++) {
            String rotated = s.substring(i) + s.substring(0, i);
            
            if (isValid(rotated)) {
                answer++;
            }
        }
        return answer;
    }
    
    private boolean isValid(String str) {
        Deque<Character> stack = new ArrayDeque<>();
        
        for (char ch : str.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                
                char open = stack.pop();
                
                if (ch == ')' && open != '(') return false;
                if (ch == '}' && open != '{') return false;
                if (ch == ']' && open != '[') return false;
            }
        }
        return stack.isEmpty();
    }
}