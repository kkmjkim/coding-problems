# 레벨2-월간2: 괄호 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque  # 리스트로 뒤에서 매번 pop하는 방법도 있음

def solution(s):
    if len(s) % 2 == 1:
        return 0

    answer = len(s)
    pair = {'(':')', '{':'}', '[':']'}

    for i in range(len(s)):  # 회전
        temp = deque(s[i:] + s[:i])
        stack = []
        while temp:  # 하나씩 보기
            popped = temp.popleft()
            if popped in pair:
                stack.append(popped)
            elif not stack:
                answer -= 1
                break
            elif popped == pair[stack[-1]]:
                stack.pop()
            else:
                answer -= 1
                break

    return answer


print(solution("}]()[{"))  # 2
