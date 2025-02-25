import sys

# Recursion Err 대응
sys.setrecursionlimit(10**6)

n = int(input())

def fact(n):
    return n * fact(n-1) if n>1 else 1

print(fact(n))
