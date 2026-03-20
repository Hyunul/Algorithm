import sys
from collections import deque

input = sys.stdin.readline
q = deque()

n = int(input())
for _ in range(n):
    cmd = input().strip().split()

    if cmd[0] == 'push_front':
        q.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        q.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if len(q) > 0:
            print(q.popleft())
        else:
            print('-1')
    elif cmd[0] == 'pop_back':
        if len(q) > 0:
            print(q.pop())
        else:
            print('-1')
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if len(q) > 0:
            print('0')
        else:
            print('1')
    elif cmd[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print('-1')
    elif cmd[0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print('-1')