import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * (n+1)
def dfs(v):
    visited[v] = True
    cnt = 0
    for nxt in g[v]:
        if not visited[nxt]:
            cnt += 1
            cnt += dfs(nxt)
    return cnt

print(dfs(1))