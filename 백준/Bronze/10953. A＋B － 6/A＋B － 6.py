import sys
input = sys.stdin.readline

t = int(input())
t_list = []
for _ in range(t):
    a, b = map(int, input().split(','))
    t_list.append(a + b)

print('\n'.join(map(str, t_list)))