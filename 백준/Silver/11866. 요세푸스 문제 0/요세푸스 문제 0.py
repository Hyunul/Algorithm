import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
l = deque(i for i in range(1, n+1))
result = []
for _ in range(n):
    l.rotate(-(k-1))
    result.append(l[0])
    l.popleft()
answer = ', '.join(str(s) for s in result)
print("<" + answer + ">")