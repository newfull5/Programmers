"""
def solution(s)
  answer = []
  abc = ""
  for i in range(len(s)):
      answer.append(ord(s[i:i+1]))
    
  answer.sort()
  answer.reverse()

  for i in range(0,len(answer)):
      abc+=(chr(answer[i]))
      
  return abc
"""
#2022.11.12
def solution(s):
    return ''.join(sorted(s, reverse=True))
