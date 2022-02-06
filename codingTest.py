from kit.graph.rooms import solution

p1 = [
    [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
]

ans = [
    3
]

for a, res in zip(p1, ans):
    sol = solution(a)
    print(True if sol == res else sol)