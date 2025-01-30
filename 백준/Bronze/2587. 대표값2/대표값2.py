total_list = []

for _ in range(5):
    temp = int(input())
    total_list.append(temp)

avg = sum(total_list) // 5
total_list.sort()
med = total_list[2]
print(avg)
print(med)