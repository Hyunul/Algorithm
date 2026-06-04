from collections import deque
def solution(food):
    answer = '0'
    d1 = deque()
    d2 = deque()
    for i in range(1, len(food)):
        temp = food[i] // 2
        if temp == 0:
            continue
        d1.appendleft(str(i)*temp)
        d2.append(str(i)*temp)
    answer = ''.join(d2) + '0' + ''.join(d1)
    return answer