def solution(n):
    answer = 0
    answer = sorted(str(n), reverse=True)
    answer = int("".join(answer))
    return answer