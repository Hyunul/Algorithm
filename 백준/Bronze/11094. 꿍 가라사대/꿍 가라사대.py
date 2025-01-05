n = int(input())

for i in range(n):
    order = input()
    # Simon says = 10 // 출력에는 공백도 포함이므로 10:
    if order[:10] == "Simon says":
        print(order[10:])