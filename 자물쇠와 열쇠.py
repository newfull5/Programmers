import numpy as np

def solution(key, lock):

    def rotate(key):

        answer = [[0]*n for a in range(n)]

        for i in range(n):
            for j in range(n):
                answer[j][n-i-1] = key[i][j]

        return answer

    m = len(key)
    n = len(lock)

    # key 값 패딩 탬플릿
    arr = [[0]*(2*n+m-2) for _ in range((2*n+m-2))]

    # 넘파이 배열로 변환
    arr = np.array(arr)

    # 중간에 key 삽입
    arr[(n-1):-(n-1),(n-1):-(n-1)] = key

    # lock배열 0 1 반전
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 1:
                lock[i][j] = 0
            else:
                lock[i][j] = 1

    for i in range(m+n-1):
        for j in range(m+n-1):
            temp = arr[i:i+n,j:j+n].tolist()
            for _ in range(4):
                temp = rotate(temp)

                if temp == lock:
                    return True
    return False
