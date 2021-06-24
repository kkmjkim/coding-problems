# 레벨2-팁스타운: 예상 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()


print(solution(8, 4, 7))  # 3
