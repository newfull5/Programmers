def calc_distance(prsent_loc, number):
    if prsent_loc == number:
        return 0
    
    if number == 2:
        if prsent_loc in [1,5,3]:
            return 1
        if prsent_loc in [4,6,8]:
            return 2
        if prsent_loc in [7,0,9]:
            return 3
        if prsent_loc in [10,11]:
            return 4
        
    if number == 5:
        if prsent_loc in [2,4,6,8]:
            return 1
        if prsent_loc in [1,3,7,0,9]:
            return 2
        if prsent_loc in [10, 11]:
            return 3
        
    if number == 8:
        if prsent_loc in [5,7,9,0]:
            return 1
        if prsent_loc in [2,4,6,10,11]:
            return 2
        if prsent_loc in [1,3]:
            return 3
        
    if number == 0:
        if prsent_loc in [10,11,8]:
            return 1
        if prsent_loc in [5,7,9]:
            return 2
        if prsent_loc in [2,4,6]:
            return 3
        if prsent_loc in [1,3]:
            return 4

def solution(numbers, hand):
    # *=10, #=11
    answer = []
    left, right = 10, 11
    for number in numbers:
        if number in [1,4,7]:
            answer.append('L')
            left = number
            continue
        if number in [3,6,9]:
            answer.append('R')
            right = number
            continue
            
        left_distance = calc_distance(left, number)
        right_distance = calc_distance(right, number)
        if left_distance == right_distance:
            if hand == 'left':
                answer.append('L')
                left = number
            if hand == 'right':
                answer.append('R')
                right = number
        if left_distance < right_distance:
            answer.append('L')
            left = number
        if left_distance > right_distance:
            answer.append('R')
            right = number
    
    return ''.join(answer)
