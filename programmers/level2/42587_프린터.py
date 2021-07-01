# 레벨2-스택/큐: 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        # cur가 max가 아니라면
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
