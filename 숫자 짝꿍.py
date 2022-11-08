from collections import Counter

def solution(X, Y):
    answer = ''
    X = Counter(X)
    Y = Counter(Y)
    y_keys = Y.keys()
    
    for k, v in X.items():
        if k in y_keys:
            answer += k*min(X[k], Y[k])
            
    if not answer:
        return '-1'
    if list(set(answer)) == ['0']:
        return '0'
    return ''.join(sorted(answer, reverse=True))
