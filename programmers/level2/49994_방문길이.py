# 레벨2-SWC~18: 방문 길이
# https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    s = set()
    d = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x, y, nx, ny))
            s.add((nx, ny, x, y))
            x, y = nx, ny
    return len(s)//2


print(solution("ULURRDLLU"))  # 7
print(solution("LULLLLLLU"))  # 7

# 집합 활용 -> 있는지 체크 안 해도 됨
