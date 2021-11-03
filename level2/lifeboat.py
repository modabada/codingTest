# https://programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque


def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))
    while people:
        weight = people.popleft()
        while True:
            if not people:
                break
            tmp = people.pop()
            if tmp + weight > limit:
                people.append(tmp)
                break
            weight += tmp
        answer += 1
    return answer
