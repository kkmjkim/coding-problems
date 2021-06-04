# 연습문제: 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950

# 정확성: 100 / 100
def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]

    return arr1


print(solution([[1, 2], [3, 4]], [[11, 22], [33, 44]]))
