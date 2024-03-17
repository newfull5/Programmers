from collections import defaultdict

def solution(keymaps, targets):
    diction = defaultdict(int)

    for keymap in keymaps:
        for i, v in enumerate(keymap):
            if diction[v] == 0:
                diction[v] = i+1
                continue

            if diction[v] > i+1:
                diction[v] = i+1

    answer = []
    for target in targets:
        total = [diction[t] for t in target]
        if 0 in total:
            answer.append(-1)
        else:
            answer.append(sum(total))

    return answer
