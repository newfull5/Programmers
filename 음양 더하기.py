def solution(absolutes, signs):
    return sum([absolutes[i] for i in range(len(absolutes)) if signs[i]]) - sum([absolutes[i] for i in range(len(absolutes)) if not signs[i]])
