# 레벨3-그래프: 순위
# https://programmers.co.kr/learn/courses/30/lessons/49191

# https://velog.io/@tjdud0123/%EC%88%9C%EC%9C%84-python
from collections import defaultdict

def solution(n, results):
    answer = 0
    wins = defaultdict(set)
    loses = defaultdict(set)

    for a, b in results:
        wins[a].add(b)
        loses[b].add(a)

    for i in range(1, n + 1):
        for loser in wins[i]:
            loses[loser] |= loses[i]  # set union
        for winner in loses[i]:
            wins[winner] |= wins[i]

    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))  # 2
# hash 이용
