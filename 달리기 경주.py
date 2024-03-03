def solution(players, callings):
    diction = {}
    
    for i, player in enumerate(players):
        diction[player] = i
        
    for calling in callings:
        idx = diction[calling]
        diction[calling] -= 1
        diction[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
        
    return players
