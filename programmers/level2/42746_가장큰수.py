# 레벨2-정렬: 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = list(map(str, numbers))
    # 1000 이하의 수 -> 4자리로 바꿔줌
    numbers.sort(key=lambda x: (x*3)[:4], reverse=True)
    answer = int(''.join(numbers))  # 0000 -> 0
    return str(answer)


print(solution([3, 30, 34, 5, 9]))  # "9534330"
