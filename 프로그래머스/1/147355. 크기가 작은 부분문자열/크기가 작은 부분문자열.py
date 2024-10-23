def solution(t, p):
    answer = 0
    t_list = list(t)
    for i in range(len(t)+1 - len(p)):
        calc = t_list[i:i+len(p)]
        if ''.join(calc) <= p:
            answer += 1
    return answer