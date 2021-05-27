# 레벨1: 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

# 정확성: 66.7 / 100
def solution(n, lost, reserve):
    answer = n - len(lost)
    done = 0  #
    for i in reserve:
        if i > 1 and (i - 1) in lost and done != i - 1:
            answer += 1
            done = i - 1
        elif i < n and (i + 1) in lost:
            answer += 1
            done = i + 1

    return answer


print(solution(7, [1, 2, 7], [3, 5, 6]))  # 6

# # 정확성: 50 / 100
# def solution(n, lost, reserve):
#     answer = n - len(lost)
#     count = 0
#     array = [1] * n
#
#     # 리스트 정리
#     for i in reserve:
#         array[i - 1] += 1
#     for i in lost:
#         array[i - 1] -= 1
#
#     # 2들을 기준으로 앞이나 뒤가 0이면 1로 바꿔라
#     for i in reserve:
#         if i > 1 and array[i - 2] == 0:
#             count += 1
#             array[i - 2], array[i - 1] = 1, 1
#         elif i < n and array[i] == 0:
#             count += 1
#             array[i - 1], array[i] = 1, 1
#
#     answer += count
#
#     return answer
#