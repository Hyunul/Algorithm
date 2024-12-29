h, m, s = map(int, input().split(" "))
add_s = int(input())

s += add_s
if s > 59:
    temp = s // 60
    m += temp
    s = s % 60
if m > 59:
    temp = m // 60
    h += temp
    m = m % 60
if h > 23:
    h = h % 24

print(h, m, s)