import sys
input = sys.stdin.readline

isbn = input().strip()
idx = isbn.index('*')

total = 0
for i in range(13):
    if i == idx:
        continue
    digit = int(isbn[i])
    if i % 2 == 0:
        total += digit
    else:
        total += digit * 3

for x in range(10):
    if idx % 2 == 0:
        test = total + x
    else:
        test = total + x*3

    if test % 10 == 0:
        print(x)
        break