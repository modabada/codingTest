# https://programmers.co.kr/learn/courses/30/lessons/49190#qna

def solution(arrows):
    v = 0
    e = 0
    prev = -1
    for arrow in arrows:
        if prev != arrow:
            e += 1
            v += 1
        prev = arrow
    print(v, e)
    return (2 - v + e)

p1 = [
    [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
]

ans = [
    3
]