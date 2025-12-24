import math

def solution(progresses, speeds):
    result = []
    taken = []
    
    for i in range(len(progresses)):
        taken.append(math.ceil((100 - progresses[i]) / speeds[i]))

    cnt = 1
    std = taken[0]
    for j in range(len(taken) - 1):
        if taken[j+1] <= std:
            cnt += 1
        else:
            result.append(cnt)
            std = taken[j+1]
            cnt = 1
    result.append(cnt)
    return result
