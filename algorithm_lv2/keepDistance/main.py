def solution(places):
    answer = []
    for e in places:
        try:
            for y in range(0, 5):
                for x in range(0, 5):
                    if e[y][x] == 'P':
                        if not check(x, y, e):
                            answer.append(0)
                            x = y = 5
        except IndexError:
            continue
        answer.append(1)
    return answer


def check(x, y, e):
    for posY in range(y, y + 3 if y < 2 else 5):
        for posX in range(x, x + 3 if x < 2 else 5):
            if posY == y and posX == x:
                continue
            if e[posY][posX] == 'P':
                if y == posY and e[y][x + 1] == 'X':
                    continue
                if x == posX and e[y + 1][x] == 'X':
                    continue
                return False
    return True
