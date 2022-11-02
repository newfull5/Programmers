def check_speakable(bab):
    words = ['aya', 'woo', 'ye', 'ma']
    
    for word in words:
        if word in bab:
            return check_speakable(bab.replace(word, ' '))
    else:
        if bab.replace(' ', ''):
            return False
        return True


def solution(babbling):
    answer = 0
    
    for bab in babbling:
        if check_speakable(bab):
            answer += 1
            
    return answer
