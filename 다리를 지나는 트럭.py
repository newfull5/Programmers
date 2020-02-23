'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    on_bridge = []
    on_bridge = deque(on_bridge)
    cnt = 0
    deq = deque(truck_weights)
    while True:        
        if not deq:
            break
        else:
            
            cnt += 1
            if len(on_bridge) == bridge_length:
                on_bridge.pop()
            if len(on_bridge) < bridge_length and sum(on_bridge) < weight:
                on_bridge.appendleft(deq.popleft())
                if sum(on_bridge) > weight:
                    deq.appendleft(on_bridge.popleft())
                    on_bridge.appendleft(0)
            elif len(on_bridge) < bridge_length and sum(on_bridge) >= weight:
                on_bridge.appendleft(0)
    return cnt + bridge_length
'''
#2020.02.23
import collections

def solution(bridge_length, weight, truck_weights):

    truck_weights = collections.deque(truck_weights)
    deq = collections.deque([])

    cnt = 0
    while True:
        if not truck_weights:
            break
        if len(deq) == bridge_length:
            deq.pop()
        if sum(deq) + truck_weights[0] > weight:
            deq.appendleft(0)
        else:
            deq.appendleft(truck_weights.popleft())

        cnt += 1
        
    return cnt+bridge_length
