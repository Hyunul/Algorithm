import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
arr = deque(range(1, n+1))
result = []

while arr:
    arr.rotate(-(k-1))
    result.append(arr.popleft())

print("<" + ', '.join(map(str, result)) + ">")