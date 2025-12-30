import sys
input = sys.stdin.readline

n = int(input())
n_list = []
for i in range(n):
    a, b = map(int, input().split(' '))
    txt = f"Case #{i+1}: {a+b}"
    n_list.append(txt)

print('\n'.join(map(str, n_list)))