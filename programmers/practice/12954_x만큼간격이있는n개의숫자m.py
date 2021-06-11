# 연습문제: x만큼 간격이 있는 n개의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12954

# 정확성: 100 / 100
def solution(x, n):  # -5, 3 --> [-5, -10, -15]
    return [x * i for i in range(1, n+1)]


print(solution(-5, 3))
