def solution(board, moves):
    answer = 0
    basket = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m - 1] != 0:
                basket.append(board[i][m - 1])
                board[i][m - 1] = 0
                break
        for i in range(1, len(basket)):
            if basket[i] is basket[i - 1]:
                print(basket[i], basket[i - 1])
                del basket[i]
                del basket[i - 1]
                answer += 2
    return answer
