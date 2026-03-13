import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def calc(n):
    n100 = n // 100
    n10 = (n % 100) // 10
    n1 = (n % 10)
    
    result = (n1 * 100) + (n10 * 10) + n100
    return result

print(max(calc(a), calc(b)))