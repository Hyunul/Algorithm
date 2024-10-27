def solution(n):
    n_list = []
    answer = 0
    while 1:
        if n > 1:
            n_remain = n % 3
            n = n // 3
            n_list.append(n_remain)
        elif n == 1:
            n_list.append(n)
            break
        else:
            break
            
    for i in range(len(n_list)):
        m = n_list.pop(-1)
        answer += m * 3 ** i
        print(m, answer)
        
    return answer