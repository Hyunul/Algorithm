import sys
input = sys.stdin.readline

def dfs(start):
    if len(picked) == 6:
        print(*picked)
        return
    
    for i in range(start, len(nums)):
        picked.append(nums[i])
        dfs(i+1)
        picked.pop()

while True:
    arr = list(map(int, input().split()))

    if arr[0] == 0:
        break

    k = arr[0]
    nums = arr[1:]
    picked = []

    dfs(0)
    print()