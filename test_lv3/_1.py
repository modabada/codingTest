def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    # [ùO nX, ùO nO, ùX nX, ùX nO]
    num = [[0] * 4 for _ in range(len(sticker))]
    num[-1][1] = sticker.pop()
    while sticker:
        n = sticker.pop()
        prev = num.pop()

        num[-1][0] = max(prev[0], prev[1])
        num[-1][1] = prev[0] + n

        num[-1][2] = max(prev[2], prev[3])
        num[-1][3] = prev[2] + n

    num[0][1] = 0
    return max(num[0])

p1 = [
    [14, 6, 5, 11, 3, 9, 2, 10],
    [1, 3, 2, 5, 4],
    [10]
]
ans = [
    36,
    8,
    10
]