n = int(input())
n_list = []

for i in range(n):
    temp = input()
    if 'S' in temp:
        n_list.append(temp)
    
if len(n_list) == 1:
    print(n_list[0])