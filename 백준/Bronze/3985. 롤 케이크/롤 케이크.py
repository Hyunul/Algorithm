l = int(input())
n = int(input())

chk_list = [0] * l
expect = {}
result = {}
for i in range(1, n+1):
    cnt = 0
    a, b = map(int, input().split())
    expect[i] = b+1-a
    for j in range(a-1, b):
        if chk_list[j] == 0:
            chk_list[j] = i
            cnt += 1
    result[i] = cnt
    
print(max(expect,key=expect.get))
print(max(result,key=result.get))