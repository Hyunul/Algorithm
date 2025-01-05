n = int(input())
n_list = list(map(int, input().split(" ")))
cnt = 0

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for j in range(len(n_list)):
    if n_list[j] > 1 and is_prime(n_list[j]):
        cnt += 1

print(cnt)