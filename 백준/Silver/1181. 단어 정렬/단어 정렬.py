import sys
input = sys.stdin.readline

n = int(input())
arr = set()

for _ in range(n):
    arr.add(input().strip())
arr = sorted(arr, key=lambda x: (len(x), x))

for item in arr:
    print(item)