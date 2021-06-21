# 레벨2-해시: 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution2(clothes):
    answer = 1
    style = {}

    for i in clothes:
        if i[1] not in style:
            style[i[1]] = 1
        else:
            style[i[1]] += 1
    for i in style.values():
        answer *= (i + 1)
    return str(answer - 1)


print(solution2([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
