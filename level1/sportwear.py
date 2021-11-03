# https://programmers.co.kr/learn/courses/30/lessons/42862


def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    lost, reserve = sorted(lost - reserve), sorted(reserve - lost)
    for e in reversed(lost):
        for lend in range(e + 1, e - 2, -1):
            if lend in reserve:
                while reserve.pop() != lend: pass
                lost.pop()
                break
    return n - len(lost)
