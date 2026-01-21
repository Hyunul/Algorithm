import sys
input = sys.stdin.readline

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

n, k = map(int, input().split())

print(fact(n) // (fact(n-k) * fact(k)))