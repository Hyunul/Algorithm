import sys
input = sys.stdin.readline

n = int(input())
total_score = []
for _ in range(n):
    arr = list(input().rstrip())
    score = 0
    temp = 0
    for item in arr:
        if item == 'X':
            temp = 0
        else:
            temp += 1
            score += temp
    total_score.append(score)

for i in total_score:
    print(i)