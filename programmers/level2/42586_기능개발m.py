# 레벨2-스택/큐: 기능 개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

# 정확성: 27.3 / 100.0
def solution(progresses, speeds):
    answer = []
    count = 1
    p0 = progresses.pop(0)
    s0 = speeds.pop(0)
    while progresses:
        if -((100 - p0) // s0) <= -((100 - progresses[0]) // speeds[0]):
            count += 1
        else:
            answer.append(count)
            count = 1
        p0 = progresses.pop(0)
        s0 = speeds.pop(0)
    answer.append(count)

    return answer


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]
