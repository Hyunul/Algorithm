def fact(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

n_list = list(str(fact(int(input()))))
cnt = 0
for i in range(len(n_list)-1, 0, -1):
    if n_list[i] != '0':
        break
    else:
        cnt += 1
print(cnt)