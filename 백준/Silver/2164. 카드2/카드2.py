import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
l = deque(i for i in range(1, n+1) )

while len(l) > 1:
    l.popleft()
    l.append(l.popleft())
print(l[0])