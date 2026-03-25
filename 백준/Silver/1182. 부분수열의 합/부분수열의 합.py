import sys
input = sys.stdin.readline

def dfs(start):
    global count
    if picked and sum(picked) == s:
        count += 1
    
    for i in range(start, n):
        picked.append(nums[i])
        dfs(i+1)
        picked.pop()

n, s = map(int, input().split())
nums = list(map(int, input().split()))

picked = []
count = 0

dfs(0)
print(count)