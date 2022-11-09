"""
def solution(absolutes, signs):
    return sum([absolutes[i] for i in range(len(absolutes)) if signs[i]]) - sum([absolutes[i] for i in range(len(absolutes)) if not signs[i]])
"""
#2022.11.09

def solution(absolutes, signs):
    return sum([num if sign else num*-1 for num, sign in zip(absolutes, signs)])
