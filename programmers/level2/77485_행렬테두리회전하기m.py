# 레벨2-Dev21: 행렬 테두리 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/77485

# 정확성: 100.0 / 100.0
def solution(rows, columns, queries):
    answer = []
    mat = [[(i) * columns + (j +1) for j in range(columns)] for i in range(rows)]
    for query in queries:
        r1, c1, r2, c2 = query
        r1 -= 1
        r2 -= 1
        c1 -= 1
        c2 -= 1
        prev = mat[r1 + 1][c1]
        m = prev
        for i in range(c1, c2):
            next = mat[r1][i]
            mat[r1][i] = prev
            prev = next
            if prev < m:
                m = prev
        for i in range(r1, r2):
            next = mat[i][c2]
            mat[i][c2] = prev
            prev = next
            if prev < m:
                m = prev
        for i in range(c2, c1, -1):
            next = mat[r2][i]
            mat[r2][i] = prev
            prev = next
            if prev < m:
                m = prev
        for i in range(r2, r1, -1):
            next = mat[i][c1]
            mat[i][c1] = prev
            prev = next
            if prev < m:
                m = prev
        answer.append(m)
    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))  # [8, 10, 25]
