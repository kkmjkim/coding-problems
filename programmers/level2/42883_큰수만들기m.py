# 레벨2-탐욕법: 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883

# 정확성: 83.3 / 100.0
def solution(number, k):
    answer = ''
    left = len(number) - k
    while True:
        n = len(number) - left + 1

        # slice & convert to int (just to find the index)
        candidates = [int(i) for i in number[:n]]

        j = max(range(len(candidates)), key=lambda i: candidates[i])
        answer += str(number[j])
        left -= 1
        number = number[j+1:]
        
        if len(number) == left:
            answer += number
            break
    return answer


print(solution('4177252841', 4))  # "3234"


# # 정확성: 83.3 / 100.0
# def solution(number, k):
#     answer = ''
#     left = len(number) - k
#     start = 0
#     end = k
#     number = [int(i) for i in number]
#
#     while left:
#         candidates = number[start:end+1]
#
#         # 나머지 모두 처리
#         if end == len(number) and len(candidates) == left:
#             answer += "".join(str(i) for i in candidates)
#             break
#
#         # argmax
#         j = start + max(range(len(candidates)), key=lambda i: candidates[i])
#
#         answer += str(number[j])
#         left -= 1
#         start = j + 1
#         end += 1
#
#     return answer