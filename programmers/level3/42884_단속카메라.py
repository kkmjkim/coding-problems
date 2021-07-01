# 레벨3-탐욕법: 단속 카메라
# https://programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30001
    answer = 0
    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]
    return answer