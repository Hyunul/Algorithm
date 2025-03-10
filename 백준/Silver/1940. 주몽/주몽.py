n = int(input())
m = int(input())
n_list = list(map(int, input().split()))

n_list.sort()
cnt = 0
left, right = 0, len(n_list) -1

while left < right:
    sum_num = n_list[left] + n_list[right]
    if sum_num < m:
        left += 1
    elif sum_num > m:
        right -= 1
    else:
        left += 1
        right -= 1
        cnt += 1

print(cnt)