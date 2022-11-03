def solution(my_string, num1, num2):
    my_string = list(my_string)
    num1_char = my_string[num1]
    num2_char = my_string[num2]
    
    my_string[num1] = num2_char
    my_string[num2] = num1_char
    
    return ''.join(my_string)
