# https://programmers.co.kr/learn/courses/30/lessons/60058


def solution(p):
    answer = ''
    if check(p):
        return p
    # 1
    if p is answer:
        return answer
    # 2
    u = ''
    v = 0
    for i, e in enumerate(p):
        v += 1 if e == '(' else -1
        if v == 0:
            u = p[:i + 1]
            v = p[i + 1:]
            break
    # 3
    if check(u):
        answer = u + solution(v)
    # 4
    else:
        answer = '(' + solution(v) + ')' + ''.join(['(' if e == ')' else ')' for e in u[1:-1]])
    return answer


def check(s):
    n = 0
    for e in s:
        n = n + (1 if e == "(" else -1)
        if n < 0:
            return False
    return n == 0
