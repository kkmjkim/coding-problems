# 연습문제: 핸드폰 번호 가리기
# https://programmers.co.kr/learn/courses/30/lessons/12948

# 정확성: 100 / 100
def solution(phone_number):
    answer = "*" * len(phone_number[:-4])
    answer += phone_number[-4:]

    return answer


print(solution("4321"))
