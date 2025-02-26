r = 31
m = 1234567891

n = int(input())
st = input()
answer = 0 

for i in range(n):
    num = ord(st[i]) - 96
    answer += num * (r ** i)

print(answer % m)