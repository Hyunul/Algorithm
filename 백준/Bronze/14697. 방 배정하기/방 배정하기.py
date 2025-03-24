a, b, c, n = map(int, input().split())

remain = n % c
if remain % a == 0 or remain % b == 0:
    print("1")
else:
    print("0")