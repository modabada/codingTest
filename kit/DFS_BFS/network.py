# https://programmers.co.kr/learn/courses/30/lessons/43162


def solution(n, computers):
    answer = 0
    group = [False] * n
    
    for i in range(n):
        if group[i]:
            continue
        stack = [i]
        visited = []
        answer += 1
        while stack:
            inx = stack.pop()
            group[inx] = True
            visited.append(inx)
            for j in range(n):
                if inx == j:
                    continue
                if computers[inx][j] == 0:
                    continue
                if j in visited:
                    continue
                stack.append(j)
    return answer
