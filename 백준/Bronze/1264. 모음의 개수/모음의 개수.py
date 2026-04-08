import sys
input = sys.stdin.readline

arr = ['a','e','i','o','u']
while True:
    cmd = list(input().lower())
    if cmd[0] == '#':
        break

    cnt = 0
    for i in range(len(cmd)):
        if cmd[i] in arr:
            cnt += 1
    
    print(cnt)