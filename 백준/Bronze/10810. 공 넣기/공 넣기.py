import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = [0 for _ in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split())
    n_list[i-1:j] = [k] * (j-i+1)

print(*n_list)