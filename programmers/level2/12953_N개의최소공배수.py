# 레벨2-연습: N개의 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12953

import math


def solution(num):
    answer = num[0]
    for n in num:
        answer = n * answer // math.gcd(n, answer)
    return answer


print(solution([2,6,8,14]))  # 168
