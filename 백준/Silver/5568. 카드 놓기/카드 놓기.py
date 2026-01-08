n = int(input())
k = int(input())

cards = [input().strip() for _ in range(n)]
used = [False] * n
result = set()

def backtrack(depth, current):
    if depth == k:
        result.add(current)
        return

    for i in range(n):
        if not used[i]:
            used[i] = True
            backtrack(depth + 1, current + cards[i])
            used[i] = False

backtrack(0, "")
print(len(result))