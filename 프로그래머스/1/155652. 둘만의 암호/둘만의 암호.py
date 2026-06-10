def solution(s, skip, index):
    answer = ''
    for word in s:  # a u k k s
        step = 0
        num = ord(word)
        
        while step < index:
            num += 1
            if num > ord('z'):
                num = ord('a')
            if chr(num) in skip:
                continue
            step += 1
        answer += chr(num)
        
    return answer