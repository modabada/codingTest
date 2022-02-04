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

# 그래프의 접근 자체는 플로이드-워샬 알고리즘으로 접근
# 기존 플로이드-워샬의 경우, 거리비교로 값을 갱신
# s가m을 이기고, m이 e에게 질 경우, 다시말해 s > m, m > e일 경우 s > e가 성립(s가 e를 이김)
# 후에 선수 한명에게 있는 None의 개수(본인과의 대결결과는 모름)가 1인 경우를 합

p1 = [
    5,
]
p2 = [
    [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
]
ans = [
    2
]