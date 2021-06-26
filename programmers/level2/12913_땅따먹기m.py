# 레벨2-연습: 땅따먹기
# https://programmers.co.kr/learn/courses/30/lessons/12913

# 정확성: 59.8
# 효율성: 40.2
# 합계: 100.0 / 100.0
def solution(land):
    # answer = 0
    cur_max = land[0]
    for i in range(1, len(land)):
        cur_max = [land[i][j] + max(cur_max[:j] + cur_max[j+1:]) for j in range(4)]
    return max(cur_max)


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))  # 16
