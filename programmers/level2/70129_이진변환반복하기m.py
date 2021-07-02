# 레벨2-월간1: 이진 변환 반복하기
# https://programmers.co.kr/learn/courses/30/lessons/70129

# 정확성: 100.0 / 100.0
def solution(s):
    answer = [0, 0]
    while s != "1":
        answer[0] += 1
        sum_zeros = s.count("0")
        answer[1] += sum_zeros
        s = str(bin(len(s) - sum_zeros)[2:])
    return answer


print(solution("110010101001"))  # [3,8]