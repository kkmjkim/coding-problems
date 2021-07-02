# 레벨2-Dev21: 행렬 테두리 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []
    S = [[(i * columns + j + 1) for j in range(columns)] for i in range(rows)]
    for r1, c1, r2, c2 in queries:
        temp = S[r1 - 1][c1 - 1]  # 처음에 변경되는 값 유지
        minv = temp  # 현재 회전에서의 최솟값 변수
        for u in range(r1 - 1, r2 - 1):  # 왼쪽 테두리 값 이동
            S[u][c1 - 1] = S[u + 1][c1 - 1]
            minv = min(minv, S[u + 1][c1 - 1])
        for l in range(c1 - 1, c2 - 1):  # 아래쪽 테두리 값 이동
            S[r2 - 1][l] = S[r2 - 1][l + 1]
            minv = min(minv, S[r2 - 1][l + 1])
        for d in range(r2 - 1, r1 - 1, -1):  # 오른쪽 ..
            S[d][c2 - 1] = S[d - 1][c2 - 1]
            minv = min(minv, S[d - 1][c2 - 1])
        for r in range(c2 - 1, c1 - 1, -1):  # 위쪽 ..
            S[r1 - 1][r] = S[r1 - 1][r - 1]
            minv = min(minv, S[r1 - 1][r - 1])
        S[r1 - 1][c1] = temp
        answer.append(minv)
    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))  # [8, 10, 25]
