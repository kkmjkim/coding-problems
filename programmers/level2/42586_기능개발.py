# 레벨2-스택/큐: 기능 개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while progresses:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:  # 이전에서 끊긴 거라면
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


print(solution([95, 98, 90, 93, 95], [1, 1, 1, 1, 1]))
