# https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ''
    while n > 0:
        n, mod = divmod(n, 3)
        if mod == 0:
            n -= 1
            mod = 4
        answer += str(mod)
    return answer[::-1]
