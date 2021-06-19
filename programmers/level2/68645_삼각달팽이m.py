# 레벨2-월간1: 삼각 달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645

# 정확성: 100.0 / 100.0
def solution(n):
    answer = []
    temp = [[0]*i for i in range(1, n+1)]  # 0으로 초기화
    row, col = -1, 0
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    idx = 0

    for i in range(n*(n+1)//2):
        next_row = row + dr[idx]
        next_col = col + dc[idx]
        # 정리 필요
        if not (0 <= next_row < n and 0 <= next_col < len(temp[row]) and temp[next_row][next_col] == 0):
            idx = (idx + 1) % 3  # 방향 전환
            next_row = row + dr[idx]
            next_col = col + dc[idx]
        row = next_row
        col = next_col
        temp[row][col] = i + 1

    for i in range(n):
        answer += temp[i]

    return str(answer)
