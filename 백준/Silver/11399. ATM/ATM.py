import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

temp = 0
result = 0
for i in lst:
    temp += i
    result += temp
print(result)