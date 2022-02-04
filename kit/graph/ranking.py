# https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3

def solution(n, results):
    graph = [[None] * n for _ in range(n)]
    while results:
        res = results.pop()
        graph[res[0] - 1][res[1] - 1] = True
        graph[res[1] - 1][res[0] - 1] = False

    for m in range(n):
        for s in range(n):
            for e in range(n):
                if graph[s][m] and graph[m][e]:
                    graph[s][e] = True
                    graph[e][s] = False
    return sum([1 for e in graph if e.count(None) == 1])

p1 = [
    5,
]
p2 = [
    [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
]
ans = [
    2
]