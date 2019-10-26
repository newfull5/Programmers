def solution(phone_book):
    for i in range(0, len(phone_book)):
        for j in range(0, len(phone_book)):
            if i != j:
                if phone_book[i] == phone_book[j][:(len(phone_book[i]))]:
                    return False
    
    return True
