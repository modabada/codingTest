from level3.stepping_bridge import solution


p1 = [
    [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
]
p2 = [
    3
]
ans = [
    3
]

for a, b, res in zip(p1, p2, ans):
    sol = solution(a, b)
    print(True if sol == res else sol, res)