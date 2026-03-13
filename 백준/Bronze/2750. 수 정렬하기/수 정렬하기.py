import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    cmd = int(input())
    arr.append(cmd)
arr.sort()

for item in arr:
    print(item)