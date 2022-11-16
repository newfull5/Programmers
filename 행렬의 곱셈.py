'''
#2020.05.05
def solution(arr1, arr2):
    arr3 = list(map(list, zip(*arr2)))
    answer = []
    
    for i in range(0, len(arr1)):
        arr = []    
        for j in range(0, len(arr2[0])):
            temp = 0
            for k in range(0, len(arr3[0])):
                temp += arr1[i][k]*arr3[j][k]

            arr.append(temp)
        answer.append(arr)
    
    return answer
'''
#2022.11.16
import numpy as np

def solution(arr1, arr2):
    return np.dot(np.array(arr1), np.array(arr2)).tolist()
