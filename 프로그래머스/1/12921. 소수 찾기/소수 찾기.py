def solution(n):
    a = [False, False] + [True] * (n-1)
    for i in range(2, int(n ** 0.5) + 1):
        if a[i]:
            a[i*i:n+1:i] = [False] * len(a[i*i:n+1:i])
    return sum(a)