import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    s = input()
    l = []
    for c in s:
        if c == "(":
            l.append(c)
        elif c == ")":
            if len(l) != 0:
                l.pop()
            else:
                print("NO")
                break
    else:
        if len(l) == 0:
            print("YES")
        else:
            print("NO")