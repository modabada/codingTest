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
            heappush(prio, jobs[inx])
            inx += 1
            continue
        if prio:
            tmp = heappop(prio)
            time += tmp[1]
            answer += time - tmp[0]
        else:
            time = jobs[inx][0]
    return answer / length
