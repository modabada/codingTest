# programmers.co.kr/learn/courses/30/lessons/64061
# 인형뽑기
# 인형을 뽑아 바구니로 옮김, 바구니에 인형이 연속되어 쌓이면 사라짐
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
