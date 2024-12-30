n = int(input())
time_list = []
for i in range(n+1):
    time, job = input().split(" ")
    if job != "teacher":
        time_list.append(time)
    else:
        teacher = time

dead_line = input()
cnt = 0

for j in range(n):
    if time_list[j] >= teacher and time_list[j] >= dead_line:
        cnt += 1
print(cnt)