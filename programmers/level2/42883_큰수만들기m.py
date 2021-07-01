# 레벨2-탐욕법: 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883

# 정확성: 83.3 / 100.0
def solution(number, k):
    answer = ''
    left = len(number) - k
    while True:
        n = len(number) - left + 1

        # slice & convert to int (just to find the index)
        candidates = [int(i) for i in number[:n]]

        j = max(range(len(candidates)), key=lambda i: candidates[i])
        answer += str(number[j])
        left -= 1
        number = number[j+1:]
        
        if len(number) == left:
            answer += number
            break
    return answer


print(solution('4177252841', 4))  # "775841"

##################################################################################################


# 정확성: 83.3 / 100.0
def solution2(number, k):
    answer = ''
    number = list(map(int, number))
    right = len(number) - k - 1
    while number:
        if right == 0:  # 이제 한개만 찾으면 될 때
            idx = number.index(max(number))
            answer += str(number[idx])
            return answer
        else:
            idx = number.index(max(number[:-right]))
            answer += str(number[idx])
            del number[:idx+1]
        right -= 1


print(solution('4177252841', 4))  # "775841"
