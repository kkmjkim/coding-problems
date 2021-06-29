# 레벨2-연습: 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924

# 정확성: 70.0
# 효율성: 30.0
# 합계: 100.0 / 100.0
def solution(n):
    answer = 1
    for i in range(1, n // 2 + 1):
        sum = i
        j = i + 1
        while sum < n:
            sum += j
            j += 1
            if sum == n:
                answer += 1

    return answer


print(solution(15))  # 4
