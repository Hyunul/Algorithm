a, b, c, m = map(int, input().split())

tired = 0
work = 0
for i in range(24):
    if tired < 0:
        tired = 0
    # 일해도 피로도가 M보다 작으면 일처리
    if tired + a <= m:
        # 1시간 일하면 피로도 A만큼 증가, 일처리 B만큼 증가
        tired += a
        work += b
    else:
        # 1시간 쉬면 피로도 C만큼 감소
        tired -= c
        
print(work)