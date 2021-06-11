# 연습문제: 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947

# 정확성: 100 / 100
def solution(x): # int
    sumX = 0
    for i in str(x):
        sumX += int(i)

    return x % sumX == 0


print(solution(18))  # True
print(solution(28))  # False
