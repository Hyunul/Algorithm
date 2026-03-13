import sys
input = sys.stdin.readline

n = int(input())
st = []
for _ in range(n):
    cmd = input().strip().split()

    if cmd[0] == 'push':
        st.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(st) > 0:
            print(st.pop())
        else:
            print('-1')
    elif cmd[0] == 'size':
        print(len(st))
    elif cmd[0] == 'empty':
        print(0 if len(st) > 0 else 1)
    elif cmd[0] == 'top':
        print(st[-1] if len(st) > 0 else -1)