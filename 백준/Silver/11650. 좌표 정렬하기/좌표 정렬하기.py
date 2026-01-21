import sys
input = sys.stdin.readline

n = int(input())
line = []
for _ in range(n):
    a, b = input().split()
    line.append((int(a), int(b)))

line.sort(key=lambda x: (x[0], x[1]))

for i in line:
    print(i[0], i[1])