n = int(input())
m = int(input())
n_list = list(map(int, input().split()))

cnt = 0

for i in range(n-1):
    for j in range(i+1, n):
        if n_list[i] + n_list[j] == m:
            cnt += 1
print(cnt)