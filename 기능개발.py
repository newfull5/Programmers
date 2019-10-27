def solution(progresses, speeds):
    days = []
    for i in range(0, len(progresses)):
        days.append(0)

    for i in range(0, len(progresses)):
        while progresses[i] < 100:
            progresses[i] = progresses[i] + speeds[i]
            days[i] += 1

    answer = []
    answerr= []

    first = 0

    for i in range(0, len(days)):
        if first < days[i]:
            answer.append(days[:i])
            first = days[i]

    for i in range(0, len(answer)-1):
        answerr.append(len(answer[i+1]) - len(answer[i]))

    answerr.append(len(days) - len(answer[-1]))

    return answerr



