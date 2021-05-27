# 레벨1: K번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748

# 정확성: 100.0 / 100.0
def solution(array, commands):
    answer = []

    # 먼저 정렬 후 처리
    array = [i for i in enumerate(array)]
    array.sort(key=lambda i: i[1])

    for command in commands:
        index = 0
        while command[2]:
            if (command[0] - 1) <= array[index][0] <= command[1] - 1:
                command[2] -= 1
            index += 1

        answer.append(array[index-1][1])
        print(2)

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))  # [5, 6, 3]
