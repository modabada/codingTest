# https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3#
from collections import deque as queue


def solution(priorities, location):
    inx = 0
    answer = 1
    length = len(priorities)
    priorities = queue(priorities)
    while True:
        max_v = max(priorities)
        while max_v in priorities:
            j = priorities.popleft()
            print(inx, inx % length)
            if j == max_v:
                if inx % length == location:
                    return answer
                priorities.append(0)
                answer += 1
                inx += 1
            else:
                priorities.append(j)
                inx += 1
