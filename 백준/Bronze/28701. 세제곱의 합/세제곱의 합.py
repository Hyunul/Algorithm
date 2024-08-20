n = int(input())

n_sq = 0
n_sq3 = 0
for i in range(1, n+1):
    n_sq += i
    n_sq3 += (i*i*i)

print(n_sq)
print(n_sq * n_sq)
print(n_sq3)