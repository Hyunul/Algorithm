import sys
input = sys.stdin.readline

x = int(input())
n = int(input())

n_list = []
for _ in range(n):
    a, b = map(int, input().split())
    n_list.append(a*b)

if x == sum(n_list):
    print("Yes")
else:
    print("No")