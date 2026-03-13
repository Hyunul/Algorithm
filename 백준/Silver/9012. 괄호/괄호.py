import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    cmd = input().strip()
    cnt = 0
    valid = True
    for i in cmd:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                valid = False
                break
            cnt -= 1
    print("YES" if valid and cnt == 0 else "NO")