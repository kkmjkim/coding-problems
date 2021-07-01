# 레벨2-월간1: 삼각 달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645

# 정확성: 100.0 / 100.0
from itertools import chain


def solution(n):
    answer = [[0]*i for i in range(1,n+1)]
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    r, c = -1, 0
    start = 1
    for i in range(n):
        for j in range(n-i, 0, -1):
            r += dr[i % 3]
            c += dc[i % 3]
            answer[r][c] = start
            start += 1
    return list(chain(*answer))


print(solution(5))  # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
