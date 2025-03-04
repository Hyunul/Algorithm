def compare(a, b):
    return -1 if a + b > b + a else 1 if a + b < b + a else 0

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if compare(x, pivot) == -1]
    middle = [x for x in arr if compare(x, pivot) == 0]
    right = [x for x in arr if compare(x, pivot) == 1]
    return quicksort(left) + middle + quicksort(right)

def solution(numbers):
    numbers = list(map(str, numbers))  # 숫자를 문자열로 변환
    numbers = quicksort(numbers)  # 퀵 정렬 사용
    result = ''.join(numbers)  # 정렬된 숫자들을 이어붙이기
    return '0' if result[0] == '0' else result  # 0이 여러 개면 "0" 하나만 반환