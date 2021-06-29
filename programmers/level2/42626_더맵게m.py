# 레벨2-힙: 다리를지나는트럭
# https://programmers.co.kr/learn/courses/30/lessons/42626

# 정확성: 76.2
# 효율성: 23.8
# 합계: 100.0 / 100.0
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
