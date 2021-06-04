# 연습문제: 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    # 함수를 완성하세요
    if a > b:
        a, b = b, a

    return sum(range(a, b+1))


print(solution(3, 5))
print(solution(3, 3))
