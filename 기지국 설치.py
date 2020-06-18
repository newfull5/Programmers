'''
import math

def solution(N, stations, W): 
    breakpoint = 0
    ans = 0

    for num in stations:
        ans += math.ceil(((num-W-1)-breakpoint)/(1+(2*W)))
        breakpoint = num + W

    if breakpoint < N:
        ans += math.ceil((N-breakpoint)/(1+(2*W)))

    return ans
'''
'''
#동시에 이렇게도 풀어 보았다. 아래의 방법으로 푸는 것이 실수가 적을듯 하다.
import math

def solution(N, stations, W):
    stations = [W*-1] + stations
    stations.append(N+W+1)
    ans = 0
    
    for i in range(0,len(stations)-1):
        if stations[i+1] - stations[i] > W*2:
            ans += math.ceil(((stations[i+1] - stations[i]) - (1+W*2))/(1+(2*W)))
            
    return ans
'''
#2020.05.13
import math

def solution(N, stations, W):
    checkpoint = 0
    cnt = 0

    for a in stations:
        cnt += math.ceil(((a-W)-1 - checkpoint)/((W*2)+1))
        checkpoint = a+W

    if (N - checkpoint) > 0:
        cnt += math.ceil((N - checkpoint)/((W*2)+1))
    
    return cnt
