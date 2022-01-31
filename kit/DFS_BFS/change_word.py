# https://programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = list()
    queue = deque()
    queue.append((begin, 0))

    while queue:
        element = queue.popleft()
        visited.append(element[0])
        for word in words:
            cnt = 0
            for x, y in zip (word, element[0]):
                if x != y:
                    cnt += 1
            if cnt == 1:
                if word == target:
                    return element[1] + 1
                elif word[0] not in visited:
                    print(element[1])
                    queue.append((word, element[1] + 1))
    return 0
