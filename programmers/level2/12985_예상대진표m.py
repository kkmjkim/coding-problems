# 레벨2-팁스타운: 예상 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985

# 정확성: 100.0 / 100.0
import math


def solution(n,a,b):
    answer = int(math.log(n, 2))
    while n > 2:
        bool_a = 0 < a <= (n/2)
        bool_b = 0 < b <= (n/2)
        if bool_a != bool_b:
            return answer
        answer -= 1
        n /= 2
        a %= n
        b %= n
    return answer


print(solution(8, 4, 7))  # 3
