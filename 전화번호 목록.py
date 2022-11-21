'''
def solution(phone_book):
    for i in range(0, len(phone_book)):
        for j in range(0, len(phone_book)):
            if i != j:
                if phone_book[i] == phone_book[j][:(len(phone_book[i]))]:
                    return False
    return True
'''
'''
#2020.04.03
def solution(phone_book):
    phone_book = sorted(phone_book, key = lambda phone_book: len(phone_book))
    
    for i in range(0, len(phone_book)-1):
        length = len(phone_book[i])
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:length]:
                return False
    return True
'''
'''
#2021.07.23
def check(phone_book):
    
    phone_book.sort()
    
    for i in range(0, len(phone_book)-1):
        if (phone_book[i] == phone_book[i+1][:len(phone_book[i])]):
            return False
    return True

def solution(phone_book):
    return check(phone_book)
'''
#2022.11.21
def solution(phone_book):
    phone_book = sorted(phone_book, key = lambda x: len(x))
    phone_book = sorted(phone_book)
    
    for i in range(0, len(phone_book)-1):
        word1, word2 = phone_book[i], phone_book[i+1]
        if len(word1) > len(word2):
            continue
        if word1 == word2[:len(word1)]:
            return False
    return True
