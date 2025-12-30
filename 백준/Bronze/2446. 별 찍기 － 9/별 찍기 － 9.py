n = int(input())

for i in range(2 * n - 1):
    dist = abs(n - 1 - i)
    space = n - 1 - dist
    star = 2 * dist + 1
    print(' ' * space + '*' * star)
