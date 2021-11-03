# https://programmers.co.kr/learn/courses/30/lessons/86052
def solution(grid):
    answer = []
    width = len(grid[0])
    height = len(grid)
    # board = [[[False] * 4] * width] * height  <- 메모리주소 복사로 배열 요소들이 독립되지 않음
    board = [[[False for _ in range(4)] for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            for d in range(4):
                # shoot
                y = i
                x = j
                direction = d
                length = 0
                while True:
                    if board[y][x][direction]:
                        if length != 0:
                            answer.append(length)
                        break

                    board[y][x][direction] = True
                    length += 1

                    if direction == 0:
                        y = (y if y != 0 else height) - 1
                    elif direction == 1:
                        x = x + 1 if x + 1 < width else 0
                    elif direction == 2:
                        y = y + 1 if y + 1 < height else 0
                    else:
                        x = (x if x != 0 else width) - 1

                    if grid[y][x] == 'R':
                        direction = direction + 1 if direction != 3 else 0
                    elif grid[y][x] == 'L':
                        direction = direction - 1 if direction != 0 else 3
    return sorted(answer)
