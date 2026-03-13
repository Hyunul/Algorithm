import sys
input = sys.stdin.readline

arr = list(input().strip().upper())
count = {}

for item in arr:
    count[item] = count.get(item, 0) + 1

max_val = max(count.values())
answer = []

for k, v in count.items():
    if max_val == v:
        answer.append(k)

print("?" if len(answer) > 1 else answer[0])