# 레벨3-그래프: 순위
# https://programmers.co.kr/learn/courses/30/lessons/49191

# https://velog.io/@tjdud0123/%EC%88%9C%EC%9C%84-python
def solution(n, results):
    chart = [[0] * n for _ in range(n)] # 승패표
    WIN, LOSE = 1, -1
    for i, j in results: # 내입장 wind = 상대방 lose
        chart[i-1][j-1], chart[j-1][i-1] = WIN, LOSE

    for me in range(n):
        # 그 값이 WIN일 때마다 행번호 담아라 (= 누구한테 이겼는지)
        wins = [opp for opp, rst in enumerate(chart[me]) if rst == WIN]
        while wins:
            loser = wins.pop()
            # (0, 1), (1, 4) -> (0, 4)
            for opp, rst in enumerate(chart[loser]):
                if rst == WIN and chart[me][opp] == 0:
                    chart[me][opp], chart[opp][me] = WIN, LOSE
                    wins.append(opp)

    return len(['know' for x in chart if x.count(0) == 1])


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))  # 2
