def solution(x):
    
    char = str(x)
    abc = 0
    
    for i in range(len(char)):
        abc = abc + int(char[i])
        
    return x % abc == 0
