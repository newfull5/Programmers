"""
def solution(phone_number):
    
    abc = []
    adc = ""
    abc = phone_number

    for i in range(len(phone_number)-4):
       adc += '*'
    
    return (adc+phone_number[-4:])
"""
#2022.11.12
def solution(phone_number):
    return '*'*len(phone_number[:-4])+phone_number[-4:]
