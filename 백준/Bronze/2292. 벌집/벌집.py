import sys
input = sys.stdin.readline

n = int(input()) # 몇번째 방까지?

cnt = 1
max_num = 1

while n > max_num:
    max_num += 6 * cnt
    cnt += 1

print(cnt)