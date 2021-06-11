# 연습문제: 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    return x % sum(int(i) for i in str(x)) == 0


print(solution(18))  # True
print(solution(28))  # False
