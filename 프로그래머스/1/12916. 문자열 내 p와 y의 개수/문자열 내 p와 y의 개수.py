def solution(s):
    answer = True
    s = s.lower()
    p = s.count("p")
    y = s.count("y")
    
    if p == 0 and y == 0:
        return True
    
    if p != y:
        return False

    return True