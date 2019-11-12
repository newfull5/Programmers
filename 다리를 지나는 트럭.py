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
