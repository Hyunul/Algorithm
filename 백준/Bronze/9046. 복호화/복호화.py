import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = input().strip()
    cnt = [0] * 26

    for ch in s:
        if ch != ' ':
            cnt[ord(ch) - ord('a')] += 1
    max_count = max(cnt)
    if cnt.count(max_count) > 1:
        print('?')
    else:
        print(chr(cnt.index(max_count) + ord('a')))