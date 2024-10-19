def solution(a, b):
    answer = 0
    
    x = min(a, b)
    y = max(a, b)

    while x < y+1:
        answer += x
        x += 1
    
    return answer