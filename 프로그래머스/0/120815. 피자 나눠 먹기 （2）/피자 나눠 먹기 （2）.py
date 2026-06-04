def solution(n):
    x = 1
    while 1:
        # 피자가 6조각
        # n = 사람 수
        # n이 같은 수의 피자 조각을 먹도록 하는 x는?
        if (x * 6) % n == 0:
            break
        x += 1
    return x