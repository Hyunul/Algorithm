n = int(input())
q = []
for i in range(n):
    temp = list(input().split())
    if len(temp) > 1:
        q.append(temp[1])
    elif temp[0] == 'front':
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    elif temp[0] == 'pop':
        if len(q) != 0:
            print(q.pop(0))
        else:
            print(-1)
    elif temp[0] == 'size':
        print(len(q))
    elif temp[0] == 'empty':
        if len(q) != 0:
            print(0)
        else:
            print(1)
    elif temp[0] == 'back':
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)