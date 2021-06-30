# 레벨2-스택/큐: 주식 가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    size = len(prices)
    answer = [0] * size
    # 마지막은 0
    for i in range(size-1):
        answer[i] += 1
        for j in range(i+1, size-1):
            if prices[j] >= prices[i]:
                answer[i] += 1
            else:
                break
    return answer


print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
