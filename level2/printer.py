# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections  import deque as queue


def solution(priorities, location):
    inx = 0
    answer = 1
    length = len(priorities)
    priorities = queue(priorities)
    while True:
        maxV = max(priorities)
        while maxV in priorities:
            j = priorities.popleft()
            if j == maxV:
                if inx % length == location:
                    return answer
                priorities.append(0)
                answer += 1
                inx += 1
            else:
                priorities.append(j)
                inx += 1
