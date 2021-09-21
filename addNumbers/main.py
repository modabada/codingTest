# https://programmers.co.kr/learn/courses/30/lessons/86051
def solution(numbers):
    inter = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} - set(numbers)
    answer = 0
    for e in inter:
        answer += e
    return answer
