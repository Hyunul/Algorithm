import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
gcd = math.gcd(a, b)
lcd = a * b // gcd

print(gcd)
print(lcd)