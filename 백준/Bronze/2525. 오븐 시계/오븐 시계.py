h, m = map(int, input().split())
need_time = int(input())

m += need_time

if m // 60 > 0:
    h += m // 60
    m = m % 60

if h // 24 >= 0:
    h = h % 24

print(h, m)