# 레벨2-SWC~18: 배달
# https://programmers.co.kr/learn/courses/30/lessons/12978

# 정확성: 100.0 / 100.0
import heapq


def solution(N, road, K):
    answer = 0
    distances = [987654321] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))  # (노드, 거리)
        graph[b].append((a, c))

    q = []
    heapq.heappush(q, (0, 1))  # (거리, 노드)
    distances[1] = 0
    while q:
        dist, cur = heapq.heappop(q)
        if distances[cur] < dist:
            continue
        # 인접 노드
        for i in graph[cur]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                # update distance
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    for i in distances:
        if i <= K:
            answer += 1
    return answer


print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))  # 4
# 그냥 다익스트라 문제
