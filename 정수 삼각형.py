"""
def solution(triangle):
    triangle = triangle[::-1]

    current = triangle[0].copy()
    triangle.remove(triangle[0])

    for arr in triangle:
        temp = []
        for i in range(0, len(current)-1):
            temp.append(max(current[i],current[i+1]) + arr[i])
        current=temp
        
    return current[0]
"""
'''
#2020.11.15
def solution(triangle):
    triangle = list(map(lambda x: [0] + x + [0], triangle))

    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])-1):
            triangle[i+1][j+1] += max(triangle[i][j], triangle[i][j+1])

    return max(triangle[-1])
'''

def solution(triangle):
    for i in range(1, len(triangle)):
        triangle[i-1] = [0] + triangle[i-1] + [0]
        
        for j in range(len(triangle[i])):
            triangle[i][j] += max([triangle[i-1][j], triangle[i-1][j+1]])
            
    return max(triangle[-1])
