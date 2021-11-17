def solution(money):
    answer = 0
    for first in [False, True]:
        dp = [[0, 0] for i in range(len(money))]
        if first:
            dp[0][1] = money[0]

        for i in range(1, len(money) - 1):
            dp[i][0] = max(dp[i-1])
            dp[i][1] = dp[i-1][0] + money[i]

        if first:  # 첫번째집 턴경우 마지막집은 못턴다.
            dp[-1][0] = max(dp[-2][0], dp[-2][1])
            dp[-1][1] = 0
        else:
            dp[-1][0] = 0
            dp[-1][1] = dp[-2][0] + money[-1]
        answer = max(answer, max(dp[-1]))
    return answer


print(solution([0, 0, 0, 3, 0, 3 ,4]))