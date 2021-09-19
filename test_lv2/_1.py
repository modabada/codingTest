def solution(s):
    n = 0
    for e in s:
        n = n + (1 if e == "(" else -1)
        if n < 0:
            return False
    return n == 0
