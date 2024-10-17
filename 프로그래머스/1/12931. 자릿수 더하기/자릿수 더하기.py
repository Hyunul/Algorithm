def solution(n):
    answer = 0

    n_list = list(map(int, str(n)))

    for i in range(len(n_list)):
        answer += n_list[i]

    return answer