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
