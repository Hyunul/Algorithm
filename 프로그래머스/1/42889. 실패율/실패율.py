def solution(N, stages):
    answer = []
    people = len(stages)
    
    for stage in range(1, N+1):
        cnt = stages.count(stage)
        
        if people == 0:
            fail = 0
        else:
            fail = cnt / people
        answer.append((stage, fail))
        people -= cnt
    answer.sort(key=lambda x: (-x[1], x[0]))

    return [stage for stage, fail in answer]