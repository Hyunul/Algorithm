n = int(input())

k = 1
time = 0

while n >= 1:
    if n < k:
        k = 1
    n -= k
    k += 1
    time += 1

print(time)