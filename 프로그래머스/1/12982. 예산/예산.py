def solution(d, budget):
    answer = 0
    count = 0
    while True:
        if len(d) != 0:
            if(answer + min(d)) <= budget:
                answer += min(d)
                d.remove(min(d))
                count += 1
            else:
                break
        else:
           break
    return count