num1 = int(input())
num2 = list(input())

num_list = []

for i in range(3):
    num_list.append(int(num2[i]) * num1)

for j in range(2, -1, -1):
    print(num_list[j])

print(int("".join(num2))*num1)