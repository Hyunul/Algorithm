# def solution(s):
#     s = list(s)
#     is_even = True # 짝수여부
#     for i in range(len(s)):
#         if i != '': # 공백x
#             if is_even:
#                 s[i] = s[i].upper()
#             else:
#                 s[i] = s[i].lower()
#             is_even = not is_even
#         else:   # 공백
#             is_even = True
#     return ''.join(s)

def solution(s):
    answer = ''
    is_even = True

    for ch in s:
        if ch == ' ':
            answer += ch
            is_even = True
        else:
            answer += ch.upper() if is_even else ch.lower()
            is_even = not is_even
    return answer