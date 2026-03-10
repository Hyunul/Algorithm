import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = [i+1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    temp = n_list[j]
    n_list[j] = n_list[i]
    n_list[i] = temp
print(*n_list)