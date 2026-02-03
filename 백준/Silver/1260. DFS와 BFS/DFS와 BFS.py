import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1, n+1):
    g[i].sort()

visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for nxt in g[v]:
        if not visited[nxt]:
            dfs(nxt)
dfs(v)
print()


def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for nxt in g[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
visited = [False] * (n+1)
bfs(v)