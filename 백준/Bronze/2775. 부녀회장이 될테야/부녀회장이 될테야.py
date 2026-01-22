import sys
input = sys.stdin.readline

apt = [[0] * 15 for _ in range(15)]

for j in range(1, 15):
    apt[0][j] = j

for i in range(1, 15):
    for j in range(1, 15):
        apt[i][j] = apt[i][j-1] + apt[i-1][j]

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(apt[k][n])