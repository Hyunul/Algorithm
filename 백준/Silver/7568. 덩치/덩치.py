import sys
input = sys.stdin.readline

n = int(input())
arr = []
arr_2 = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

for i in range(len(arr)):
    k = 1
    for j in range(len(arr)):
        if i == j: # 본인은 패스
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            k += 1
    arr_2.append(k)

print(" ".join(map(str, arr_2)))