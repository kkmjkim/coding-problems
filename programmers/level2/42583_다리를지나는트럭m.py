# 레벨2-스택/큐: 다리를지나는트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583

# 정확성: 92.9 / 100.0
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    passing = deque([0] * bridge_length)

    while passing:
        answer += 1
        passing.popleft()
        if truck_weights:
            if sum(passing) + truck_weights[-1] <= weight:  # 앞에서 시작, 뒤에서 시작 쌤쌤
                passing.append(truck_weights.pop())
            else:
                passing.append(0)

    return str(answer)


print(solution(2, 10, [7,4,5,6]))

# pop을 쓰려면 마지막 조건이 꼭 필요. 여기선 if truck_weights 로.
# deque.popleft() 보다 list.pop(0)이 왜 더 빠르지?
