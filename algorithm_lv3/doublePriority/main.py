# https://programmers.co.kr/learn/courses/30/lessons/42628
from heapq import heappop, heappush


def solution(operations):
    answer = []
    maxV = 0
    for oper in operations:
        if not answer:
            if oper == 'D 1' or oper == 'D -1':
                continue
        if oper == 'D 1':
            del answer[answer.index(max(answer))]
        elif oper == 'D -1':
            heappop(answer)
        else:
            heappush(answer, int(oper[2:]))
    answer.sort() 
    return [answer[-1], answer[0]] if answer else [0, 0]
