import sys
input = sys.stdin.readline

n = int(input())
val_list = []
for _ in range(n):
    val = int(input())
    if val != 0:
        val_list.append(val)
    else:
        val_list.pop()

print(sum(val_list))