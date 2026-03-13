import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
print(min(n_list), max(n_list))