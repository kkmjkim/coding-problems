# 레벨2-월간2: 2개 이하로 다른 비트
# https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    for idx, val in enumerate(numbers):
        answer.append(((val ^ (val+1)) >> 2) + val + 1)
    return answer


print(solution([2, 7]))  # [3, 11]

