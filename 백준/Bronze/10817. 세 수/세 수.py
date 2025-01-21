n_list = list(map(int, input().split()))
max_val = max(n_list)
n_list.pop(n_list.index(max_val))
print(max(n_list))