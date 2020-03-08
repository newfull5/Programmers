'''
def solution(n):
    answer = [1,2]
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        for i in range(2,n):
            answer.append(answer[0]+answer[1])
            answer.pop(0)
    return answer[-1]%1000000007
'''
    #-----------------------
'''
def fac(num):
    if num == 0:
        return 0
    temp = 1
    for i in range(1,num+1):
        temp *= i
    return temp

def divide(num):
    temp = []
    for i in range(0, num):
        if (num-(i*2))<0:
            break
        temp.append([num-(i*2),i*2])
    return temp

def tnsduf(arr):
    left = arr[0]
    right = (arr[-1]//2)
    if left==0 or right==0:
        return 1
    return fac(right+left)//(fac(right)*fac(left))

def solution(n):
    temp = 0
    for each in divide(n):
        temp += tnsduf(each)
        
    return temp%1000000007
'''
#여유가 생기고 나면 문제의 더 많은 것이 보인다. 이렇게 쉬운문제였는데 과거의 나는 뭘한건가.
def solution(n):
    a = 1
    b = 2
    for i in range(1, n-1):
        a,b = b, a+b
    return b%1000000007
