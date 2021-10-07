def solution(grid):
    # while False in cycle, cycle.index(False)
    # 위의 두 부분에서 매 루프마다 선형탐색을 통해 False 값을 찾기 때문에 해당 시간복잡도가 크게 떨어짐
    answer = []
    width = len(grid[0])
    height = len(grid)
    cycle = [False] * 4 * height * width    # 엣지가 4방향으로 뻣어있음으로 노드마다 4개의 배열
    while False in cycle:   # 싸이클이 여러 개 있을 경울을 대비
        length = 0
        direction = cycle.index(False) % 4
        node = cycle.index(False) // 4
        y = node // width
        x = node % width
        while not cycle[(y * width + x) * 4 + direction]:   # 해당 엣지가 방문된 적이 없었음
            length += 1

            cycle[(y * width + x) * 4 + direction] = True   # 방문처리
            if direction == 0:      # 현재 방향에 따른 좌표변경
                y = (y if y > 0 else height) - 1
            elif direction == 1:
                x = x + 1 if x + 1 < width else 0
            elif direction == 2:
                y = y + 1 if y + 1 < height else 0
            else:
                x = (x if x > 0 else width) - 1

            if grid[y][x] == 'R':   # 도착한 노드에 따른 방향전환
                direction = direction + 1 if direction < 3 else 0
            elif grid[y][x] == 'L':
                direction = direction - 1 if direction > 0 else 3
        answer.append(length)   # 싸이클 길이 추가
    return sorted(answer)
