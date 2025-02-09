def solution(n, k):
    serve = n // 10
    answer = n*12000 + (k-serve)*2000
    
    return answer