def solution(s):
    matching_list = { "zero":"0", "one":"1", "two":"2", "three":"3","four":"4","five":"5","six":"6","seven":"7", "eight":"8", "nine":"9" }
    
    for i in matching_list:
        s = s.replace(i, matching_list[i])
    return int(s)