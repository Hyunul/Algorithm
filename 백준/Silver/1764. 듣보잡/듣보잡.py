import sys
input = sys.stdin.readline

n,m = map(int, input().split())

not_listen = set()
for _ in range(n):
    not_listen.add(input().strip())

result = []

for _ in range(m):
    name = input().strip()
    if name in not_listen:
        result.append(name)

result.sort()

print(len(result))
for name in result:
    print(name)