def solution(score):
    score_list = [(index, s1+s2) for index, (s1, s2) in enumerate(score)]
    score_list = (sorted(score_list, key=lambda x: x[-1], reverse=True))
    
    ranking = [1]
    for i in range(1, len(score_list)):
        idx, score = score_list[i]
        if score == score_list[i-1][-1]:
            ranking.append(ranking[i-1])
        else:
            ranking.append(i+1)
            
    answer = sorted([(ranking[i], score_list[i][0]) for i in range(len(ranking))], key=lambda x:x[-1])
    
    return [a for a,b in answer]
