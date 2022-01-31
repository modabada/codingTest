# https://programmers.co.kr/learn/courses/30/lessons/42861


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    root = dict()
    find = lambda x: x if root[x] == x else find(root[x])
    for cost in costs:
        # union
        if cost[0] not in root:
            root[cost[0]] = cost[0]
        if cost[1] not in root:
            root[cost[1]] = cost[1]

        if find(cost[0]) == find(cost[1]):
            continue

        check = cost[0] < cost[1]
        x = find(cost[0] if check else cost[1])
        y = find(cost[1] if check else cost[0])
        root[y] = x

        answer += cost[2]
    return answer
