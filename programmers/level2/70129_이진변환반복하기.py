# 레벨2-월간1: 이진 변환 반복하기
# https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]


print(solution("110010101001"))  # [3,8]
