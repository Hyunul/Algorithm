def solution(nums):
    answer = 0
    pick = len(nums) // 2
    nums = set(nums)
    if pick < len(nums):
        answer = pick
    else:
        answer = len(nums)
    return answer