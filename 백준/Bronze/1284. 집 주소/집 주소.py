import sys
input = sys.stdin.readline

while True:
    cmd = list(input().rstrip())
    cnt = len(cmd) - 1
    if cmd[0] == '0':
        break

    for item in cmd:
        if item == '1':
            cnt += 2
        elif item == '0':
            cnt += 4
        else:
            cnt += 3
    print(cnt + 2)