def solution(n):
    answer = 0
    while n > 0:
        if n - 7 > 0:
            n -= 7
        else:
            n = 0
        answer += 1
    return answer