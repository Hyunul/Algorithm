def solution(n):
    answer = 0
    ans_list = []
    for i in range(1, n):
        if n % i == 1:
            ans_list.append(i)
    
    answer = min(ans_list)
    
    return answer