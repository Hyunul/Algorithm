import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = dict()
for _ in range(n):
    a, b = input().split()
    lst[a] = b

re_lst = []
for _ in range(m):
    re_lst.append(input().rstrip())

for i in re_lst:
    print(lst[i])