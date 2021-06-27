# 레벨2-마에스터: 게임 맵 최단거리
# https://programmers.co.kr/learn/courses/30/lessons/1844

# 정확성: 69.9
# 효율성: 30.1
# 합계: 100.0 / 100.0
from collections import deque
def solution(maps):
    answer = -1  # init distance
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    queue = deque()
    queue.append((0, 0, 1))  # init
    while queue:
        r, c, dist = queue.popleft()
        if (r == len(maps) - 1) and (c == len(maps[0]) - 1):
            return dist
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < len(maps)) and (0 <= nc < len(maps[0])):  # w/i range
                if maps[nr][nc] == 1:
                    maps[nr][nc] = 0  # visited 의미 (backtracking 없으니까)
                    queue.append((nr, nc, dist + 1))
    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))  # 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))  # -1
