# 레벨2-월간2: 2개 이하로 다른 비트
# https://programmers.co.kr/learn/courses/30/lessons/77885

# 정확성: 81.8 / 100.0
def solution(numbers):
    answer = [numbers[i] + 1 for i in range(len(numbers))]

    for i in range(len(numbers)):
        diff = bin(numbers[i] ^ (answer[i])).count("1")
        while diff != 1 and diff != 2:
            answer[i] += 1
            diff = bin(numbers[i] ^ (answer[i])).count("1")

    return answer


print(solution([2, 7]))  # [3, 11]
