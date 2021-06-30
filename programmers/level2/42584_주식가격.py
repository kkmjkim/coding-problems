# 레벨2-스택/큐: 주식 가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer


print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
