import sys
input = sys.stdin.readline

def calc(i):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 3 != 0 and i % 5 == 0:
        print("Buzz")
    else:
        print(i)

arr = []
for _ in range(3):
    n = input().rstrip()
    arr.append(n)

for i in range(3):
    if arr[i].isdigit():
        calc(int(arr[i]) + (3 - i))
        break