import sys
input = sys.stdin.readline

n = int(input())
n_list = map(int, input().split())

m = int(input())
m_list = map(int, input().split())

count_dict = {}

for num in n_list:
    count_dict[num] = count_dict.get(num, 0) + 1

result = []
for num in m_list:
    result.append(str(count_dict.get(num, 0)))

print(" ".join(result))