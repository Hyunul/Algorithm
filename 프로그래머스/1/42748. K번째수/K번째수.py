def solution(array, commands):
    answer = []
    for a in range (len(commands)):
        i = commands[a][0]
        j = commands[a][1]
        k = commands[a][2]
        
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    
    return answer