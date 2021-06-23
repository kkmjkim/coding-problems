# 레벨2-스택/큐: 다리를지나는트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    answer = 0
    passing = [0] * bridge_length
    while len(passing):
        answer += 1
        passing.pop(0)
        if truck_weights:
            if sum(passing) + truck_weights[0] <= weight:
                passing.append(truck_weights.pop(0))
            else:
                passing.append(0)
    return str(answer)


print(solution(2, 10, [7, 4, 5, 6]))

# sum()이 오래 걸리면 pop할 때 빼고 append할 때 더하는 방법도 있긴 함
