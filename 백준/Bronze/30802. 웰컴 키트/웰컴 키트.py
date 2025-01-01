n = int(input())
s, m, l, xl, xxl, xxxl = map(int, input().split(" "))
t, p = map(int, input().split(" "))
cnt = 0
size_list = [s, m, l, xl, xxl, xxxl]
for item in size_list:
    if item % t == 0:
        cnt += item // t
    else:
        cnt += (item // t + 1)
    
print(cnt)
print((n//p), (n%p))