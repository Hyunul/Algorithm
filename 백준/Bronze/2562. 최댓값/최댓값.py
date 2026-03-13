import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
    cmd = int(input())
    arr.append(cmd)

print(max(arr))
print(arr.index(max(arr)) + 1)