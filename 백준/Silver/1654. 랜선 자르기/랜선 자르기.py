k, n = map(int, input().split())

lan_cable = [int(input()) for _ in range(k)]
    
answer = 0

start, end = 1, max(lan_cable)
while start <= end:
    mid = (start + end) // 2
    
    # 랜선의 개수
    sum = 0
    
    # 랜선 잘라내기
    for i in lan_cable:
        sum += i // mid
    
    # 랜선의 개수가 n 이상이면
    if sum >= n:
        # mid 아래는 필요없음
        start = mid + 1
        answer = mid
        
    # 랜선의 개수가 n 미만이면
    else:
        # mid 이상은 필요없음
        end = mid - 1
        
print(answer)