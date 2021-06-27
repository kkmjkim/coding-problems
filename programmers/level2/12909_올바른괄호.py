# 레벨2-연습: 올바른 괄호
# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    x = 0  # count 개념
    for w in s:
        if x < 0:
            break
        x = x + 1 if w == "(" else x-1 if w == ")" else x
        if w == "(":
            x = x + 1
        else:
            x = x - 1

    return x == 0


print(solution("(())()"))  # True
print(solution("(()("))  # False
