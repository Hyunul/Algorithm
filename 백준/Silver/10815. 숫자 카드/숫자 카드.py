import sys
input = sys.stdin.readline

n = int(input())
n_lst = set(map(int, input().split()))

m = int(input())
m_lst = list(map(int, input().split()))
result = [0] * m

for i in range(m):
    if m_lst[i] in n_lst:
        result[i] = 1

print(' '.join(map(str, result)))