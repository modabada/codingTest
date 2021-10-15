# https://programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    length = len(prices)
    answer = [0] * length
    for i in range(length):
        cnt = 0
        for j in range(i + 1, length):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer[i] = cnt
    return answer
