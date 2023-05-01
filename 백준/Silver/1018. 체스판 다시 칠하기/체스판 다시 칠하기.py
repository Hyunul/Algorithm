import sys
input = sys.stdin.readline

board = []
count = []
M, N = map(int, input().split())
for _ in range(M):
    board.append(list(input()))

for i in range(M - 7):
    for j in range(N - 7):
        w_count = 0
        b_count = 0
        
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != "W":
                        w_count += 1
                    else:
                        b_count += 1
                else:
                    if board[a][b] != "W":
                        b_count += 1
                    else:
                        w_count += 1
                        
        count.append(w_count)
        count.append(b_count)
        
print(min(count))