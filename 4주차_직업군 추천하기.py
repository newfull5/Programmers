def solution(table, languages, preference):
    diction = {}

    for i in range(len(languages)):
        diction[languages[i]] = preference[i]

    answer = {}

    for tab in table:
        for i,v in enumerate(tab.split()):
            if i == 0:
                lang = v
                answer[lang] = 0
                continue
            if v in languages:
                answer[lang] += (diction[v] * (6-i))

    answer = sorted(list(answer.items()), key = lambda x: (x[0]*10)[:10])

    answer = sorted(answer, key = lambda x: x[-1], reverse=True)

    return answer[0][0]
