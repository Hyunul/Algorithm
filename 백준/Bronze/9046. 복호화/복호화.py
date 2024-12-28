from collections import Counter

n = int(input())
for i in range(n):
    enc_str = input().replace(" ", "")
    cnt = Counter(enc_str).most_common()
    if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
        print("?")
    else:
        print(cnt[0][0])