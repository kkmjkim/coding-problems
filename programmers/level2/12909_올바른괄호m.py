# 레벨2-연습: 올바른 괄호
# https://programmers.co.kr/learn/courses/30/lessons/12909

# 정확성: 69.5
# 효율성: 30.5
# 합계: 100.0 / 100.0
def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif stack and stack[-1] == "(":
            stack.pop()
        else:
            return False
    if stack:
        return False
    return answer


print(solution("(())()"))  # True
print(solution("(()("))  # False
