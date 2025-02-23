n = int(input())
lv_list = sorted([int(input()) for _ in range(n)], reverse=True)[:42]

total_lv = 0
total_abil = 0
for lv in lv_list:
    total_lv += lv
    if lv >= 250:
        total_abil += 5
    elif lv >= 200:
        total_abil += 4
    elif lv >= 140:
        total_abil += 3
    elif lv >= 100:
        total_abil += 2
    elif lv >= 60:
        total_abil += 1

print(total_lv, total_abil)