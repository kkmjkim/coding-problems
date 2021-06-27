# 레벨2-연습: N개의 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12953

# 정확성: 100.0 / 100.0
def solution(arr):
    # 최소공배수 = 곱 / 최대공약수
    answer = arr.pop(0)
    while arr:
        # 최대공약수
        x, y = answer, arr.pop(0)
        answer *= y
        while y:
            x, y = y, x % y  # 4, 6 -> 6, 4 -> 4, 2 -> 2, 0
        answer /= x
    return answer


print(solution([2,6,8,14]))  # 168
