def get_unregi_word(diction, msg, index):
    return_index = 0
    
    for i in range(index+1, len(msg)+1):
        word = msg[index:i]
        if word in diction.keys():
            return_index = diction[word]
        else:
            return return_index, word[:-1], word
    return diction[msg[index:]], msg[index:], '_'

def solution(msg):
    length = 26
    diction = {}
    answer = []
    
    for i in range(1,27):
        diction[chr(i+64)] = i    
    
    idx = 0
    while idx < len(msg):
        answer_index, exist_word, new_word = get_unregi_word(diction, msg, idx)
        idx += len(exist_word)
        length += 1
        diction[new_word] = length
        answer.append(answer_index)
        
    return answer
