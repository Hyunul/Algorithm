n = int(input())
f = int(input())

init_n = n // 100 * 100
temp = init_n // f * f
if temp % 100 != 0:
    temp += f
result = temp % 100
if len(str(result)) == 1:
    result = "0" + str(result)
print(result)