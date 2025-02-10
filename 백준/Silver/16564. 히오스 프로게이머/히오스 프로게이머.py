import sys

input = sys.stdin.readline

n, k = map(int, input().split())
l = []
for _ in range(n):
    l.append(int(input()))

s = min(l)
e = max(l) + k
r = 0

while s <= e:
    m = (s + e) // 2
    sum = 0
    # list 순회
    for i in l:
        # 현재 레벨이 레벨 중앙값보다 낮으면 차이값을 sum에 합산
        if i < m:
            sum += m - i
    # sum이 총 레벨 이하라면 시작점을 중앙값 + 1로 설정하고 r값을 m으로 설정
    if sum <= k:
        s = m + 1
        r = m
    # sum이 총 레벨 초과라면 끝점을 중앙값 - 1로 설정
    else:
        e = m - 1
print(r)