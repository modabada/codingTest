# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution(n, edge):
    # 그래프 생성
    graph = [[] for _ in range(n)]
    for e in edge:
        if e[1] - 1 not in graph[e[0] - 1]:
            graph[e[0] - 1].append(e[1] - 1)
        if e[0] - 1 not in graph[e[1] - 1]:
            graph[e[1] - 1].append(e[0] - 1)
    # BFS를 구현하기 위한 변수
    visited = [False] * n
    node = [n] * n
    queue = deque()
    visited[0] = True
    node[0] = 0
    queue.append(0)
    while queue:
        n = queue.popleft()
        for e in graph[n]:
            # 방문한 적이 없을경우, 방문 + queue 추가 + node값 갱신
            if not visited[e]:
                queue.append(e)
                visited[e] = True
                if node[e] > node[n]:
                    node[e] = node[n] + 1
    far = max(node)
    return len([n for n in node if n == far])

# BFS로 접근할 경우, 모든 노드에 접근시 최단경로를 통해 접근하게됨
# 접근해가며 거리값 갱신 후 max value를 모아놓은 리스트의 길이 반환
# 쓸데없이 Counter함수 써서 고생했네

p1 = [
    6
]
p2 = [
    [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
]
ans = [
    3
]
