import math


# 입력값 n이 만약 정수 x 의 제곱이라면 x + 1 의 제곱값을 리턴, 아니면 -1 리턴
def solution(n):
    answer = 0
    n = n ** 0.5
    if round(n) == n:
        answer = (n + 1) ** 2
    else:
        answer = -1
    return answer
