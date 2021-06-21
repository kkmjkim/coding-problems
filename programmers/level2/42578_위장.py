# 레벨2-해시: 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

import collections
from functools import reduce

def solution(c):
    return str(reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1)


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
