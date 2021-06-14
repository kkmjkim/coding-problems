# 레벨1-연습문제: x만큼 간격이 있는 n개의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    return [x * i + x for i in range(n)]  # 등차수열 식 이용


print(solution(-5, 3))
