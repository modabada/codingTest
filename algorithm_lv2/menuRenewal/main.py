# https://programmers.co.kr/learn/courses/30/lessons/72411?language=python3
from itertools import combinations


def solution(orders, course):
    answer = []
    for cnt in course:
        counter = dict()
        for guest in orders:
            for e in combinations(sorted(guest), cnt):
                if e in counter:
                    counter[e] += 1
                else:
                    counter[e] = 1
        if not counter:
            continue
        most = max(counter.values())
        if most == 1:
            continue
        for e in counter:
            if counter[e] == most:
                answer.append(''.join(e))
    return sorted(answer)
