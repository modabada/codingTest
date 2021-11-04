# https://programmers.co.kr/learn/courses/30/lessons/42884


def solution(routes):
    routes.sort(key=lambda x: -x[1])
    cam = routes.pop()[1]
    answer = 1
    while routes:
        route = routes.pop()
        if route[0] > cam:
            cam = route[1]
            answer += 1
    return answer
