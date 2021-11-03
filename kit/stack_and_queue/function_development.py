# https://programmers.co.kr/learn/courses/30/lessons/42586


def solution(progresses, speeds):
    answer = []
    day = 0
    while progresses:
        day += 1
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] > 100:
                progresses[i] = 100
        cnt = 0
        while progresses and progresses[0] >= 100:
            cnt += 1
            del progresses[0]
            del speeds[0]
        if cnt > 0:
            answer.append(cnt)
    return answer
