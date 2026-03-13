import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    arr = []
    cmd = list(input().strip())
    try:
        for i in cmd:
            if i == '(':
                arr.append(i)
            else:
                arr.pop()
    except:
        print("NO")
        continue
    print("NO" if len(arr) > 0 else "YES")