# 레벨2: 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    stack = [number[0]]  # 스택 사용
    for num in number[1:]:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


print(solution("4177252841", 4))  # "775841"
