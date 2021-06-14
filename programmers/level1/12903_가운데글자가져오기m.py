# 레벨1-연습문제: 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903

# math 써도 되나 ??

# 정확성: 100 / 100
import math

def solution(s):
    i = (len(s) - 1) // 2
    j = math.ceil((len(s) - 1) / 2)
    return s[i:j+1]


print(solution("ab"))  # ab
print(solution("a"))  # a
print(solution("abcde"))  # c
