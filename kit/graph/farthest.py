# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution(n, edge):
    # �׷��� ����
    graph = [[] for _ in range(n)]
    for e in edge:
        if e[1] - 1 not in graph[e[0] - 1]:
            graph[e[0] - 1].append(e[1] - 1)
        if e[0] - 1 not in graph[e[1] - 1]:
            graph[e[1] - 1].append(e[0] - 1)
    # BFS�� �����ϱ� ���� ����
    visited = [False] * n
    node = [n] * n
    queue = deque()
    visited[0] = True
    node[0] = 0
    queue.append(0)
    while queue:
        n = queue.popleft()
        for e in graph[n]:
            # �湮�� ���� �������, �湮 + queue �߰� + node�� ����
            if not visited[e]:
                queue.append(e)
                visited[e] = True
                if node[e] > node[n]:
                    node[e] = node[n] + 1
    far = max(node)
    return len([n for n in node if n == far])

# BFS�� ������ ���, ��� ��忡 ���ٽ� �ִܰ�θ� ���� �����ϰԵ�
# �����ذ��� �Ÿ��� ���� �� max value�� ��Ƴ��� ����Ʈ�� ���� ��ȯ
# �������� Counter�Լ� �Ἥ ����߳�

p1 = [
    6
]
p2 = [
    [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
]
ans = [
    3
]
