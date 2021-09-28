def solution(w, h):
    grad = -h / w
    answer = 0
    for x in (1, w):
        answer += int(grad * x + h)
    return answer * 2
