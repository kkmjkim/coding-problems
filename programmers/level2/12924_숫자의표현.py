# 레벨2-연습: 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])


print(solution(15))  # 4

# 등차수열의 합 & 초항과 개수는 모두 자연수여야 함을 이용
# https://gkalstn000.github.io/2021/01/21/%EC%88%AB%EC%9E%90%EC%9D%98-%ED%91%9C%ED%98%84/
