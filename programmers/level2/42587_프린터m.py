# 레벨2-스택/큐: 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587

# 정확성: 100.0 / 100.0
from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque([*enumerate(priorities)])
    sort_p = deque(sorted(priorities, reverse=True))  # 내림차순
    while q:
        head = q[0]
        if head[1] == sort_p[0]:
            answer += 1
            q.popleft()
            sort_p.popleft()
            if head[0] == location:
                return answer
        else:
            q.rotate(-1)  # 꼬리로 보내
    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
