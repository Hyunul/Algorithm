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

for i in range(3):
    s = input().rstrip()
    if s.isdigit():
        calc(int(s) + (3 - i))
        break