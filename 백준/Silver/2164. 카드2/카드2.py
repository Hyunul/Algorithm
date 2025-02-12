import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
l = deque()
for i in range(1, n+1):
    l.append(i)
    
# print(l.popleft())
while len(l) > 1:
    l.popleft()
    l.append(l.popleft())
print(l[0])