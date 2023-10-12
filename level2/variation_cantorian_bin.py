# https://school.programmers.co.kr/learn/courses/30/lessons/148652

def solution(n, l, r):
    answer = 0
    for i in range(l-1, r):
        if check(i):
            answer += 1
    return answer

def check(i):
    if i < 5 and i != 2: return True
    if ((i - 2) % 5 == 0): return False
    return check(i // 5)
