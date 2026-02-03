import sys
input = sys.stdin.readline

a, b = map(int, input().split())
val = []
for _ in range(a):
    val.append(int(input()))

val.sort(reverse=True)

cnt = 0
for i in val:
    cnt += b // i
    b %= i

print(cnt)