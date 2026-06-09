def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        temp = b

        for w in words:
            if w * 2 in temp:
                break
            temp = temp.replace(w, " ")

        else:
            if temp.strip() == "":
                answer += 1

    return answer