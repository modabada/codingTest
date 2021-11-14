# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    area = [[0] * m for i in range(n)]
    for pud in puddles:
        area[pud[1] - 1][pud[0] - 1] = -1
    area[0][0] = 1
    for y in range(n):
        for x in range(m):
            if area[y][x] != -1:
                if x + 1 < m and area[y][x + 1] != -1:
                    area[y][x + 1] += area[y][x]
                if y + 1 < n and area[y + 1][x] != -1:
                    area[y + 1][x] += area[y][x]
    answer = area[n - 1][m - 1]
    return answer % 1000000007
