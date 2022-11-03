def exchange_uplow(char):
    num = ord(char)
    if num < 91:
        return chr(num+32)
    else:
        return chr(num-32)

def solution(my_string):
    return ''.join([exchange_uplow(char) for char in my_string])
