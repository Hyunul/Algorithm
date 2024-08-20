N, K, P = map(int, input().split())

bread_list = list(map(int, input().split()))
result = 0
for i in range(N):
    cnt = 0
    for j in range(K):
        if bread_list[0] == 0:
            cnt += 1
        bread_list.pop(0)
    if cnt < P:
        result += 1
print(result)