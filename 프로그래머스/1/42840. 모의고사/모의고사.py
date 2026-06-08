def solution(answers):
    answer = []
    solver_1 = [1,2,3,4,5]
    solver_2 = [2,1,2,3,2,4,2,5]
    solver_3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = {i: 0 for i in range(1, 4)}
    for i in range(len(answers)):
        if answers[i] == solver_1[i % len(solver_1)]:
            score[1] += 1
        if answers[i] == solver_2[i % len(solver_2)]:
            score[2] += 1
        if answers[i] == solver_3[i % len(solver_3)]:
            score[3] += 1
    # k = key, v = value
    for k, v in score.items():
        if v == max(score.values()):
            answer.append(k)
    return answer