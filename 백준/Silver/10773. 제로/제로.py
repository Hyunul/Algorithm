import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    cmd = int(input())
    arr.pop() if cmd == 0 else arr.append(cmd)
print(sum(arr))