# 레벨1: K번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748

# command 들어오면 정렬
def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


def solution2(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))  # [5, 6, 3]

print(solution2([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))  # [5, 6, 3]
