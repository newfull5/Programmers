"""
import re

def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    new_id = re.sub('[^a-z\d\-\_\.]','',new_id)

    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..','.')

    # 4단계
    if new_id:
        if new_id[0] == '.':
            new_id = new_id[1:]

    if new_id:
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 5단계
    else:
        new_id = 'a'

    # 6단계
    new_id = new_id[:15]

    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]
        
    return new_id
"""
#2022.11.09
import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = ''.join(re.findall('[a-z0-9-_.]', new_id))
    new_id = re.sub('\.+','.',new_id)
    new_id = re.sub('^\.', '', new_id)
    new_id = re.sub('\.$', '', new_id)
    if not new_id:
        new_id = 'a'
    if len(new_id) > 15:
        new_id = new_id[:15]
    new_id = re.sub('\.$', '', new_id)
    if len(new_id) < 3:
        new_id = new_id + new_id[-1]
    if len(new_id) < 3:
        new_id = new_id + new_id[-1]
        
    return new_id
