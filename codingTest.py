from kit.graph.farthest import solution

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