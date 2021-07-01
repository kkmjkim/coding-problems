# 레벨2-월간1: 삼각 달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution1(n):
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    b = [[0] * i for i in range(1, n+1)]
    x, y = 0, 0
    num = 1
    d = 0
    while num <= (n+1)*n // 2:
        b[y][x] = num
        ny = y + dy[d]
        nx = x + dx[d]
        num += 1
        if 0 <= ny <n and 0 <= nx <= ny and b[ny][nx] == 0:
            y, x = ny, nx
        else:
            d = (d+1) % 3
            y += dy[d]
            x += dx[d]
    return sum(b, [])


print(solution1(5))  # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]

###################################################################################################
# "To concatenate a series of iterables, consider using itertools.chain()."
from itertools import chain


def solution2(n):
    [row, col, cnt] = [-1, 0, 1]
    board = [[None] * i for i in range(1, n+1)]
    for i in range(n):  # 방향 전환이 총 n번만 일어난다는 것을 활용
        for _ in range(n-i):
            if i % 3 == 0:
                row += 1
            elif i % 3 == 1:
                col += 1
            else:
                row -= 1
                col -= 1
            board[row][col] = cnt
            cnt += 1
    return list(chain(*board))


print(solution2(5))  # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
