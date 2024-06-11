'''
def solution(routes):
    routes = sorted(routes, key = lambda x: x[-1])
    length = len(routes)
    chk = [False] * length
    answer = 0

    for i in range(length):
        if chk[i]:
            continue

        camera = routes[i][-1]
        answer += 1

        for j in range(i, length):
            if routes[j][0] <= camera and camera <= routes[j][1]:
                chk[j] = True
    return answer
'''

def check_overlab(locate, route2):
    left, right = route2
    if left <= locate <= right:
        return True
    return False

def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[-1])
    check = [False] * len(routes)
    
    for i, route in enumerate(routes):
        if check[i]:
            continue
            
        answer += 1
        locate = route[-1]
        
        for j, route2 in enumerate(routes):
            if check_overlab(locate, route2):
                check[j] = True
                
    return answer
