import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        arr.pop()
    else:
        arr.append(cmd)
print(sum(arr))