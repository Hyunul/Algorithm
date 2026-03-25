import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    cmd = input().strip()
    n = int(input())
    s = input().strip()
    
    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, s[1:-1].split(',')))
    
    rev = False
    error = False
    for i in cmd:
        if i == "R":
            rev = not rev
        else:
            if not arr:
                print("error")
                error = True
                break
            if rev:
                arr.pop()
            else:
                arr.popleft()

    if not error:
        if rev:
            arr.reverse()
        print("[" + ",".join(map(str, arr)) + "]")