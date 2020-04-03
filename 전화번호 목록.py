'''
def solution(phone_book):
    for i in range(0, len(phone_book)):
        for j in range(0, len(phone_book)):
            if i != j:
                if phone_book[i] == phone_book[j][:(len(phone_book[i]))]:
                    return False
    return True
'''
def solution(phone_book):
    phone_book = sorted(phone_book, key = lambda phone_book: len(phone_book))
    
    for i in range(0, len(phone_book)-1):
        length = len(phone_book[i])
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:length]:
                return False
    return True
