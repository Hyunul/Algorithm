import math

n = int(input())


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def pelindrom(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


while True:
    if is_prime(n) and pelindrom(n):
        print(n)
        break
    n += 1
