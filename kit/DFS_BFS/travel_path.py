# https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3


def solution(tickets):
    tickets.sort()
    visited = list()

    def dfs(route):
        for i, e in enumerate(tickets):
            if route[-1] == e[0]:
                del tickets[i]
                print(e)
                route = dfs(route + [e[1]])
        return route

    r = dfs(["ICN"])
    print(visited)
    return r

pram = [
    [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]],
    [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],
    [["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "BOO"], ["BOO", "AOO"], ["BOO", "FOO"], ["FOO", "COO"], ["COO", "ZOO"]],
    [["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "COO"], ["COO", "AOO"], ["BOO", "ZOO"]],
    [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]],
    [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]],
    [["ICN", "AOO"], ["ICN", "AOO"], ["AOO", "ICN"], ["AOO", "COO"]],
    [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
]

res = [
    ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"],
    ["ICN", "JFK", "HND", "IAD"],
    ["ICN", "AOO", "BOO", "AOO", "BOO", "FOO", "COO", "ZOO"],
    ["ICN", "AOO", "COO", "AOO", "BOO", "ZOO"],
    ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"],
    ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"],
    ["ICN", "AOO", "ICN", "AOO", "COO"],
    ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]
]
for p, r in zip(pram, res):
    sol = solution(p)
    print(sol == r)
    print(sol)
    print(r)
    print()