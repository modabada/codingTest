# https://school.programmers.co.kr/learn/courses/30/lessons/161990


def solution(wallpaper):
    top,  bottom, left, right = 50, -1, 50, -1
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[y])):
            if wallpaper[y][x] == '#':
                if y < top:
                    top = y
                if y + 1 > bottom:
                    bottom = y + 1
                if x < left:
                    left = x
                if x + 1 > right:
                    right = x + 1
    return [top, left, bottom, right]
