# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    while triangle:
        floor = triangle.pop()
        if triangle:
            for i in range(len(triangle[-1])):
                triangle[-1][i] += floor[i] if  floor[i] > floor[i + 1] else floor[i + 1]
        else:
            return floor[0]
