# 레벨2-월간2: 괄호 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/76502

# 정확성: 100.0 / 100.0
def solution(s):
    answer = 0
    if len(s) % 2 != 0:
        return 0
    pairs = {"[": "]", "{": "}", "(": ")"}
    for _ in range(len(s)):
        s = ''.join(s[1:] + s[0])
        stack = []
        for i in range(len(s)):
            if s[i] in pairs.keys():
                stack.append(s[i])
            elif stack and stack[-1] in pairs.keys():
                if s[i] == pairs[stack[-1]]:
                    stack.pop()
                else:
                    break
            else:
                break
        else:
            if not stack:
                answer += 1
    return answer


print(solution("[](){}"))  # 3
print(solution("[)(]"))  # 0
# for-else 활용
