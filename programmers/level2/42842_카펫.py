# 레벨2-완전탐색: 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

import math


def solution(brown, yellow):
    # brown, yellow, w ,h 관계 이용해서 근의 공식 구하기
    w = ((brown+4) / 2 + math.sqrt(((brown+4) / 2) ** 2 - 4 * (brown+yellow))) / 2
    h = ((brown+4) / 2 - math.sqrt(((brown+4) / 2) ** 2 - 4 * (brown+yellow))) / 2
    return [int(w), int(h)]


print(solution(24, 24))  # [8, 6]

##########################################################################################


def solution2(brown, yellow):
    for i in range(1, int(yellow ** (1 / 2)) + 1):
        # i가 약수라면
        if yellow % i == 0:
            # yellow 둘레 활용
            if 2 * (i + yellow // i) == brown - 4:
                return [yellow // i + 2, i + 2]


print(solution2(24, 24))  # [8, 6]
