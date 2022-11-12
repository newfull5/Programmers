"""
def solution(arr1, arr2):
    arr3 = []
    arr4 = []
    
    for i in range(0, len(arr1)):
        for j in range(0, len(arr1[0])):
            arr3.append(arr1[i][j] + arr2[i][j])
        arr4.append(arr3)
        arr3 = []
        
    return arr4
"""

import numpy as np

def solution(arr1, arr2):
    return (np.array(arr1) + np.array(arr2)).tolist()
