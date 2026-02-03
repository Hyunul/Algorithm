import sys
input = sys.stdin.readline

t = int(input())

zero_cnt = 0
one_cnt = 0

# 0 / 1
dp = [(0, 0)] * 41
dp[0] = (1, 0)
dp[1] = (0, 1)

for i in range(2, 41):
    dp[i] = (
        dp[i-1][0] + dp[i-2][0],
        dp[i-1][1] + dp[i-2][1]
    )

case = []
for _ in range(t):
    case.append(int(input()))

for i in case:
    print(dp[i][0], dp[i][1])