# 연습문제: 짝수와 홀수
# https://programmers.co.kr/learn/courses/30/lessons/12937

# 정확성: 100 / 100
def solution(num):
    return "Even" if num % 2 == 0 else "Odd"


print(solution(3))  # Odd
print(solution(0))  # Even
print(solution(-4))  # Even
