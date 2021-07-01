# 레벨2-연습: 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911

# 정확성: 70.0
# 효율성: 30.0
# 합계: 100.0 / 100.0
def solution(n):
    c1 = bin(n).count("1")
    while True:
        n += 1
        c2 = bin(n).count("1")
        if c2 == c1:
            return n


print(solution(78))  # 83
