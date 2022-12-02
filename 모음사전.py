from itertools import product

def solution(word):
    a = product(['0', 'A', 'E', 'I', 'O', 'U'], repeat=5)
    a = sorted(list(set([''.join(b).replace('0', '') for b in a])))
    return a.index(word)
