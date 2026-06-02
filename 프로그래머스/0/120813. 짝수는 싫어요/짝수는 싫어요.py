def solution(n):
    answer = []
    arr = [i for i in range(n+1)]
    for i in arr:
        if i % 2 > 0:
            answer.append(i)
    return answer