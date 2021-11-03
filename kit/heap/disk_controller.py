# https://programmers.co.kr/learn/courses/30/lessons/42627
from heapq import heappush, heappop


def solution(jobs):
    jobs.sort()
    prio = list()
    length = len(jobs)
    inx = 0
    time = 0
    answer = 0
    
    while length > inx or prio:
        if length > inx and time >= jobs[inx][0]:
            heappush(prio, jobs[inx][::-1])
            inx += 1
            continue
        if prio:
            tmp = heappop(prio)
            time += tmp[0]
            answer += time - tmp[1]
        else:
            time = jobs[inx][0]
    return int(answer / length)
