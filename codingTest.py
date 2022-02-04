from kit.graph.ranking import solution

p1 = [
    5,
]
p2 = [
    [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
]
ans = [
    2
]

for a, b, res in zip(p1, p2, ans):
    sol = solution(a, b)
    print(True if sol == res else sol)