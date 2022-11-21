from collections import defaultdict
import math


def calc_time(start_time, end_time):
    a,b = end_time.split(':')
    c,d = start_time.split(':')
    duration = (int(a) * 60 + int(b)) - (int(c) * 60 + int(d))
    return duration


def calc_cost(duration, fees):
    base_minute, base_cost, minute, cost = fees
    
    if duration <= base_minute:
        return base_cost
    
    duration = duration - base_minute
    return base_cost + math.ceil(duration / minute) * cost


def solution(fees, records):
    total_duration = defaultdict(int)
    io_dict = defaultdict(str)
    
    for record in records:
        time, car, c = record.split()
        if not io_dict[car]:
            io_dict[car] = time
        else:
            total_duration[car] += calc_time(io_dict[car], time)
            io_dict[car] = ''
            
    for car, time in io_dict.items():
        if not time:
            continue
        total_duration[car] += calc_time(time, '23:59')
            
    answer = sorted(((car,time) for car, time in total_duration.items()), key=lambda x: x[0])
    answer = [calc_cost(time, fees) for _, time in answer]
    return answer
