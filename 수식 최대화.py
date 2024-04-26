import re

def calc_mul(expression):
    while re.search('\-?\d+\*\-?\d+', expression):
        finded = re.search('\-?\d+\*\-?\d+', expression)
        l,r = finded.span()
        a,b = finded.group().split('*')
        expression = expression[:l] + str(int(a)*int(b)) + expression[r:]
    return expression


def calc_add(expression):
    while re.search('\d+\+\-?\d+', expression):
        finded = re.search('\d+\+\-?\d+', expression)
        l,r = finded.span()
        a,b = finded.group().split('+')
        expression = expression[:l] + str(int(a)+int(b)) + expression[r:]
    return expression
        
def calc_minus(expression):
    while re.search('\-?\d+\-\d+', expression):
        finded = re.search('\-?\d+\-\d+', expression)
        l,r = finded.span()
        splited = finded.group().split('-')
        if len(splited) == 3:
            a = int(splited[1]) * -1
            b = int(splited[2])
        elif len(splited) == 2:
            a,b = splited
        
        expression = expression[:l] + str(int(a)-int(b)) + expression[r:]
    return expression

def solution(expression):  
    return max([
        abs(int(calc_minus(calc_add(calc_mul(expression))))),
        abs(int(calc_add(calc_minus(calc_mul(expression))))),
        abs(int(calc_mul(calc_minus(calc_add(expression))))),
        abs(int(calc_minus(calc_mul(calc_add(expression))))),
        abs(int(calc_add(calc_mul(calc_minus(expression))))),
        abs(int(calc_mul(calc_add(calc_minus(expression))))),
    ])
