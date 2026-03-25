import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    q = deque((i, arr[i]) for i in range(n))
    cnt = 0

    while q:
        idx, priority = q.popleft()
        flag = False

        for x in q:
            if x[1] > priority:
                flag = True
                break

        if flag:
            q.append((idx, priority))
        else:
            cnt += 1
            if idx == m:
                print(cnt)
                break