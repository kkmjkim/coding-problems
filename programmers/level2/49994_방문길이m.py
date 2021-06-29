# 레벨2-SWC~18: 방문 길이
# https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0
    direction = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    r, c = 0, 0
    # [(r, c), (nr, nc)] 지점 저장
    visited = []

    for d in dirs:
        nr = r + direction[d][0]
        nc = c + direction[d][1]
        # next가 out of range면
        if nr < -5 or nr > 5 or nc < -5 or nc > 5:
            continue
        # 양방향 있나 체크
        elif [(r, c), (nr, nc)] in visited or [(nr, nc), (r, c)] in visited:
            # move만
            r = nr
            c = nc
        else:
            visited.append([(r, c), (nr, nc)])
            answer += 1
            r = nr
            c = nc
    return answer


print(solution("ULURRDLLU"))  # 7
print(solution("LULLLLLLU"))  # 7
