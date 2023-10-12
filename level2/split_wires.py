# https://school.programmers.co.kr/learn/courses/30/lessons/86971

def solution(n, wires):
    answer = n
    wires.sort()
    for ignore in wires:
        g = dict()
        for w in wires:
            if w[0] not in g:
                g[w[0]] = list()
            if w[1] not in g:
                g[w[1]] = list()
            g[w[0]].append(w[1])
            g[w[1]].append(w[0])
        
        v = set()
        def dfs(node):
            v.add(node)
            for neighbor in g[node]:
                if neighbor in v: continue
                if set([neighbor, node]) == set(ignore): continue
                dfs(neighbor)
        dfs(wires[0][0])
        d = abs(len(v) -(n - len(v)))
        # print('ignore', ignore)
        # print(v, d)
        if answer > d:
            answer = d
            
    return answer
