"""
#2020.04.27
import re

def solution(files):
    q = re.compile('\d+')
    concat = []
    
    for file in files:
        span = q.search(file).span()
        a = file[:span[0]].upper()
        b = int(file[span[0]:span[1]])

        concat.append((a,b,file))
        
    concat = sorted(concat, key = lambda x: x[1])
    concat = sorted(concat, key = lambda x: x[0])
    
    return [c for a,b,c in concat]
"""
'''
import re

q = re.compile('\d+')

arr = []
for file in files:
    sss = q.search(file)
    arr.append((file[:sss.start()].lower(), int(sss.group()),file))

arr = sorted(arr, key = lambda x: x[1])
arr = sorted(arr, key = lambda x: x[0])

return [c for a,b,c in arr]
'''
#2022.12.02
import re

def solution(files):
    lists = []
    for file in files:
        head = re.findall('[a-zA-Z.\-\\s]+', file)[0]
        number = re.findall('^[^\d]*(\d+)', file)[0]
        lists.append((file, head.lower(), int(number)))
    
    lists = sorted(lists, key=lambda x: x[2])
    lists = sorted(lists, key=lambda x: x[1])
    return [file for file, head, number in lists]
