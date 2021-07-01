# 레벨2-완전탐색: 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842


def solution(brown, yellow):
    answer = []
    # 약수 구하기
    p = [(i, yellow//i) for i in range(1, yellow+1) if (yellow % i==0 and (i <= yellow//i))]
    # 일치하는 쌍 반환
    for i in p:
        if brown == (2*i[0] + 2*i[1] + 4):
            return [i[1] + 2, i[0] + 2]


print(solution(24, 24))  # [8, 6]
