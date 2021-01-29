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
