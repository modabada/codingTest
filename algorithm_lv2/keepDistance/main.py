# https://programmers.co.kr/learn/courses/30/lessons/81302?language=python3
def solution(places):
    answer = []
    for e in places:
        try:
            for y in range(0, 5):
                for x in range(0, 5):
                    if e[y][x] == 'P':
                        if not checkRule(x, y, e):
                            answer.append(0)
                            raise KeyboardInterrupt
        except KeyboardInterrupt:
            continue
        answer.append(1)
    return answer


def checkRule(x, y, e):
    for posY in range(y - 2 if y > 1 else 0, y + 3 if y < 2 else 5):
        start = x - (2 - abs(posY - y))
        end = x + (3 - abs(posY - y))
        for posX in range(0 if start < 0 else start, 5 if end > 4 else end):
            if posY == y and posX == x:
                continue
            if e[posY][posX] == 'P':
                if y == posY and e[y][posX + int((x - posX) / 2)] == 'X':
                    continue
                if x == posX and e[posY + int((y - posY) / 2)][x] == 'X':
                    continue
                if y != posY and x != posX and e[posY + (- 1 if posY > y else 1)][posX] == 'X' and \
                        e[posY][posX + (-1 if posX > x else 1)] == 'X':
                    continue
                return False
    return True
