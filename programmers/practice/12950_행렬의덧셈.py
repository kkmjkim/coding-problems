# 연습문제: 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = [[a + b for a, b in zip(c, d)] for c, d in zip(arr1, arr2)]
    return answer


print(solution([[1, 2], [3, 4]], [[11, 22], [33, 44]]))
