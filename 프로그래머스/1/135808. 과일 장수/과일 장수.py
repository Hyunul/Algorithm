def solution(k, m, score):
    answer = 0
    score.sort(reverse=1)
    
    box = []
    for item in score:
        box.append(item)
        if len(box) == m:
            answer += min(box) * m
            box = []
    return answer