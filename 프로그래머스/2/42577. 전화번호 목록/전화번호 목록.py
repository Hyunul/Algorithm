def solution(phone_book):
    hashMap = {}
    for i in phone_book:
        hashMap[i] = 1
    
    for j in phone_book:
        arr = ""
        for num in j:            
            arr += num
            if arr in hashMap and arr != j:
                return False
    return True