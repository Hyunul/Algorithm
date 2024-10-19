def solution(x):
    x = str(x)
    res = 0
    for i in range(len(x)):
        res += int(x[i])
    if int(x) % res == 0:
        return True
    else:
        return False