import sys

input = sys.stdin.readline

n = int(input())
l = []

for i in range(n):
    a = input().strip()
    
    if a.startswith("push"):
        _, b = a.split()
        l.append(b)
    elif a == "pop":
        if len(l) == 0:
            print("-1")
        else:
            print(l.pop())
    elif a == "size":
        print(len(l))
    elif a == "empty":
        if len(l) == 0:
            print("1")
        else:
            print("0")
    elif a == "top":
        if len(l) == 0:
            print("-1")
        else:
            print(l[-1])