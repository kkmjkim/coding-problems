# 레벨2-연습: 가장 큰 정사각형 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    answer = board[0][0]

    for i in range(len(board) - 1):
        for j in range((len(board[0]) - 1)):
            if board[i+1][j+1] == 1:
                board[i+1][j+1] = min(board[i][j], board[i+1][j], board[i][j+1]) + 1
                answer = max(answer, board[i+1][j+1])

    return answer ** 2


print(solution([[0,0,1,1],[1,1,1,1]]))  # 4
