def solution(name, yearning, photos):
    answer = []
    dict_map = {}
    for i in range(len(name)):
        dict_map[name[i]] = yearning[i]
        
    for photo in photos:
        score = 0
        for people in photo:
            if people in dict_map:
                score += dict_map[people]
        answer.append(score)
    return answer