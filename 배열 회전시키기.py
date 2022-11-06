def solution(numbers, direction):
    if direction == 'right':
        return [numbers.pop()] + numbers
    
    numbers.append(numbers.pop(0))
    return numbers
