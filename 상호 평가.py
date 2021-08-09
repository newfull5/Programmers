from collections import Counter
import numpy as np

def get_hakjum(num):
    if num >= 90:
        return 'A'
    if num >= 80:
        return 'B'
    if num >= 70:
        return 'C'
    if num >= 50:
        return 'D'
    return 'F'


def compute_avg(arr, min_score, max_score):
    answer = []

    for num in arr:
        if num == min_score or num == max_score:
            continue
        answer.append(num)
    if not answer:
        return 0
    return sum(answer) / len(answer)


def solution(scores):
    length = len(scores)

    self_scores = ([scores[i][i] for i in range(length)])
    self_scores = Counter(self_scores)

    min_score, max_score = 50000, 50000

    if self_scores[min(self_scores.keys())] == 1:
        min_score = min(self_scores.keys())

    if self_scores[max(self_scores.keys())] == 1:
        max_score = max(self_scores.keys())


    scores = np.array(scores)

    return(''.join([get_hakjum(compute_avg(scores[:, i], min_score, max_score)) for i in range(len(scores))]))

if __name__ == '__main__':
    scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]



