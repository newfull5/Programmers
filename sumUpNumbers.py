import re

def sumUpNumbers(inputString):
    p = re.compile('\d+')
    m = p.findall(inputString)
    m = map(int, m)
    return sum(m)
