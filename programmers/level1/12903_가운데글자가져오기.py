# 레벨1-연습문제: 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    return s[(len(s) - 1) // 2 : len(s) // 2 + 1]


print(solution("ab"))  # ab
print(solution("a"))  # a
print(solution("abcde"))  # c
