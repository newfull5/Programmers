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
