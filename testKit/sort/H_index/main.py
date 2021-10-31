# https://programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    citations.sort()
    n = len(citations)
    h = n
    while h > 0:
        if citations[n - h] < h:
            h -= 1
            continue
        if len(citations[h:]) > h:
            h -= 1
            continue
        return h
    return 0
