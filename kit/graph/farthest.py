# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque, Counter

def solution(n, edge):
    graph = [[] for _ in range(n)]
    for e in edge:
        if e[1] not in graph[e[0] - 1]:
            graph[e[0] - 1].append(e[1])
        if e[0] not in graph[e[1] - 1]:
            graph[e[1] - 1].append(e[0])
    for e in graph:
        print(e)

    return
    node = [n] * n
    visited = [False] * n
    queue = deque()
    queue.append(1)
    node[0] = 0
    while queue:
        n = queue.popleft()
        visited[n - 1] = True
        for e in edge:
            if e[0] == n and not visited[e[1] - 1]:
                queue.append(e[1])
                if node[e[1] - 1] > node[n - 1]:
                    node[e[1] - 1] = node[n - 1] + 1
            elif e[1] == n and not visited[e[0] - 1]:
                queue.append(e[0])
                if node[e[0] - 1] > node[n - 1]:
                    node[e[0] - 1] = node[n - 1] + 1
    return Counter(node).most_common()[0][1]


p1 = [
    6
]
p2 = [
    [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
]
ans = [
    3
]

for a, b, res in zip(p1, p2, ans):
    sol = solution(a, b)
    print(True if sol == res else sol)
