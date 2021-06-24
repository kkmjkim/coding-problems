# 레벨2-연습: 행렬의 곱셈
# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]


print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
# [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
