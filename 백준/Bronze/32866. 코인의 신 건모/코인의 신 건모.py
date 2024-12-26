N = int(input())
X = int(input())

if 100 <= N and N <= 1000 and 1 <= X and X <= 99:
    temp = N - N * (X / 100)
    result = N/temp - 1
    
print(round(result * 100, 6))
