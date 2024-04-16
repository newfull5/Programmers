'''
def solution(m, musicinfos):
    def convert(string):
        string = string.replace('C#','c')
        string = string.replace('D#','d')
        string = string.replace('F#','f')
        string = string.replace('G#','g')
        string = string.replace('A#','a')

        return string

    m = convert(m)
    answer = []

    for music in musicinfos:
        a,b,c,d = music.split(',')
        d = convert(d)
        
        time = (int(b.split(':')[0]) - int(a.split(':')[0]))*60
        time += (int(b.split(':')[1]) - int(a.split(':')[1]))
        e,f = divmod(time, len(d))
        d = d*e + d[:f]
        if m in d:
            if not answer:
                answer.append([c,time])
            else:
                if answer[0][-1] < time:
                    answer = [[c,time]]
                    
    if not answer:
        return "(None)"

    return answer[0][0]
'''
import re


def replace_note(string):
    string = string.replace('C#', 'c')
    string = string.replace('D#', 'd')
    string = string.replace('F#', 'f')
    string = string.replace('G#', 'g')
    string = string.replace('A#', 'a')
    string = string.replace('B#', 'b')
    string = string.replace('E#', 'e')
    return string
    
    
def calc_timestring(time):
    h,m = time.split(':')
    return int(h)*60 + int(m)


def solution(m, musicinfos):
    answer = []
    m = replace_note(m)
    
    for idx, musicinfo in enumerate(musicinfos):
        start, end, name, melody = musicinfo.split(',')
        duration = calc_timestring(end) - calc_timestring(start)
        melody = (replace_note(melody)*10000)[:duration]
        
        if re.search(m, melody):
            answer.append([name, duration, idx])
    
    if not answer:
        return '(None)'
    
    answer = sorted(answer, key=lambda x: x[-1], reverse=True)
    answer = sorted(answer, key=lambda x: x[-2])
    name, *_ = answer.pop()
    return name
