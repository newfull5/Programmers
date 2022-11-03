def check_correct(formula):
    a,b,c,_,e = formula.split()

    if b == '+':
        return (int(a) + int(c)) == int(e)
    if b == '-':
        return (int(a) - int(c)) == int(e)

def solution(quiz):
    return ['O' if check_correct(formula) else 'X' for formula in quiz]
