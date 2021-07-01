# 레벨2-연습: 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n, count = 0):
    return n if bin(n).count("1") == count else solution(n+1, bin(n).count("1") if count == 0 else count)


print(solution(78))  # 83
