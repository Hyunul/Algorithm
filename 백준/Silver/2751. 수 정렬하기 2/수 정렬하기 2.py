import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=False)

sys.stdout.write("\n".join(map(str, arr)))