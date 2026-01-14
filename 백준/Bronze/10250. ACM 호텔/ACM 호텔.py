import sys
input = sys.stdin.readline

def calc(h, w, n):
    result_100 = (n-1) % h + 1
    result_10 = (n - 1) // h + 1
    print(result_100*100 + result_10)

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    calc(h, w, n)