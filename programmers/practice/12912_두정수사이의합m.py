# 연습문제: 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912

# 정확성: 100 / 100
def solution(a, b):
    return (a + b) * (abs(b - a) + 1) / 2


print(solution(3, 5))
print(solution(3, 3))
