# 레벨2-월간2: 2개 이하로 다른 비트
# https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    for n in numbers:
        asBin = bin(n)[2:]
        zero_loc = asBin.rfind('0')  # 오른쪽부터 첫번째 0 주소값

        if asBin[-1] == '0':  # 2^0 자리가 0이면, n+1이 정답
            answer.append(n + 1)
        else:  # 오른쪽부터) 연속된 1의 마지막 자리 x에 대해, 2^x를 더해줌, ex. if n == 10110111: 2^x = 100
            answer.append(n + (1 << (len(asBin) - zero_loc - 2)))  # = n + 2^(len(asBin) - zero_loc - 2)

    return answer


print(solution([2, 7]))  # [3, 11]
