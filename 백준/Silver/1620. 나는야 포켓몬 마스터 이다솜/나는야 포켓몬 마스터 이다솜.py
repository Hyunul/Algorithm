import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name_list = [None]
name_dict = {}

for i in range(1, n+1):
    name = input().strip()
    name_list.append(name)
    name_dict[name] = i

for _ in range(m):
    cmd = input().strip()
    if cmd.isdigit():
        print(name_list[int(cmd)])
    else:
        print(name_dict[cmd])