class Solution {
    public String solution(int[] numbers, String hand) {
        StringBuilder answer = new StringBuilder();
        
        int left = 10;
        int right = 12;
        
        for (int number : numbers) {
            int key = number == 0 ? 11 : number; // 타겟
            
            if (key == 1 || key == 4 || key == 7) {
                answer.append("L");
                left = key; // 키 누른 왼손 위치 이동
            } else if (key == 3 || key == 6 || key == 9) {
                answer.append("R");
                right = key; // 키 누른 오른손 위치 이동
            } else { // 가운데 키패드 입력
                int leftDistance = getDistance(left, key);
                int rightDistance = getDistance(right, key);
                
                if (leftDistance > rightDistance) {
                    answer.append("R");
                    right = key;
                } else if (leftDistance < rightDistance) {
                    answer.append("L");
                    left = key;
                } else { // 거리가 같을 시 어느 손 잡이?
                    if (hand.equals("right")) {
                        answer.append("R");
                        right = key;
                    } else {
                        answer.append("L");
                        left = key;
                    }
                }
            }
        }
        return answer.toString();
    }
    // 맨해든 거리 공식 : |r1-r2| + |c1-c2|
    private int getDistance(int current, int target) {
        int currentRow = (current - 1) / 3;
        int currentCol = (current - 1) % 3;

        int targetRow = (target - 1) / 3;
        int targetCol = (target - 1) % 3;

        return Math.abs(currentRow - targetRow) + Math.abs(currentCol - targetCol);
    }
}