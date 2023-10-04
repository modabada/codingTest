# https://school.programmers.co.kr/learn/courses/30/lessons/12941
def solution(A,B):
    answer = 0
    for x, y in zip(sorted(A), reversed(sorted(B))):
        answer += x * y
    return answer