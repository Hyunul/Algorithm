def get_days(month):
    days31 = [1,3,5,7,8,10,12]
    days30 = [4,6,9,11]
    days = 0

    for i in range(1, month):
        if i in days31:
            days += 31
        elif i in days30:
            days += 30
        else:
            days += 28
    return days

week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
month, day = map(int, input().split(' '))
sum_days = get_days(month) + (day - 1)
print(week[sum_days % 7])