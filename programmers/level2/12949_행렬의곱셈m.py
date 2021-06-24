# 레벨2-연습: 행렬의 곱셈
# https://programmers.co.kr/learn/courses/30/lessons/12949

# 정확성: 100.0 / 100.0
def solution(arr1, arr2):
    arr2 = list(zip(*arr2))  # transpose
    answer = [[0] * len(arr2) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[j][k]

    return answer


print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
# [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
