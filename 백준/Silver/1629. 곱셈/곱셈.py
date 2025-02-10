import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

# pow(base, exp, mod=None) => base의 exp제곱을 mod로 나눈 나머지 반환
print(pow(a, b, c))
