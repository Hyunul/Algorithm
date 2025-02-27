d= []
d.append(0)
d.append(1)
d.append(1)

def solution(n):
    for i in range(3, n+1):
        d.append((d[i-1] + d[i-2])% 1234567)
    return d[n]