# https://programmers.co.kr/learn/courses/30/lessons/62048


def solution(w, h):
    grad = -h / w
    answer = 0
    if 1 in [h, w]:
        return 0
    if h == w:
        return h * w - w
    for x in range(1, w):
        answer += int(grad * x + h)
    return answer * 2
