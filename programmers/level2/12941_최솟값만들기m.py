# 레벨2-연습: 최솟값 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12941

# 정확성: 69.6
# 효율성: 30.4
# 합계: 100.0 / 100.0
def solution(A, B):
    answer = 0
    # 오름
    A.sort()
    B.sort(reverse=True)
    # 내림
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer


print(solution([1, 4, 2], [5, 4, 4]))  # 29
