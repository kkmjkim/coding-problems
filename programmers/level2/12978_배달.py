# 레벨2-SWC~18: 배달
# https://programmers.co.kr/learn/courses/30/lessons/12978

# 부캠님 코드
from collections import defaultdict
import heapq  # 우선순위큐

def solution(N, road, K):
    graph = defaultdict(list)

    for f, t, c in road:  # 그래프 초기화
        graph[f].append((t, c))
        graph[t].append((f, c))

    fees = [float('inf')] * (N + 1)  # 1번 마을 기준 최소비용
    fees[1] = 0
    Q = [(1, fees[1])]  # 현재 마을, 현재 cost

    while Q:  # 다익스트라
        cur_n, cur_f = heapq.heappop(Q)
        if fees[cur_n] < cur_f:
            continue

        for next_n, fee in graph[cur_n]:
            if cur_f + fee < fees[next_n]:
                fees[next_n] = cur_f + fee
                heapq.heappush(Q, (next_n, cur_f + fee))

    return len([0 for f in fees if f <= K])


print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))  # 4
