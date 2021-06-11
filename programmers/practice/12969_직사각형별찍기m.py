# 연습문제: 직사각형 별찍기
# https://programmers.co.kr/learn/courses/30/lessons/12969

# 정확성: 100 / 100
a, b = map(int, input().strip().split(' '))
print(("*" * a + "\n") * b)
