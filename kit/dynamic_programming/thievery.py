def solution(money):
    answer = 0
    for first in [True, False]:
        # poket[n] = [n번째 집을 안턴 경우, 턴 경우]
        poket = [[0, 0] for _ in range(len(money))]
        if first:
            poket[0][1] = money[0]

        for i in range(1, len(money)):
            # 안털 경우 -> 이전 경우에서 큰 값을 찾으면 됨
            poket[i][0] = max(poket[i - 1])
            # 털 경우 -> 이전 경우에서 안턴 경우 + 현재 집을 턴 값
            poket[i][1] = poket[i - 1][0] + money[i]

        # 첫 집을 털면, 마지막 집을 못턺
        if first:
            poket[-1][1] = 0

        answer = max(answer, max(poket[-1]))
    return answer


# poket[n] = [[첫집O n집O, 첫집O n집X], [첫집X n집O, 첫집X n집X]]
# 위 방식으로 배열을 크게잡고 반복횟수 줄이기 -> 실패,
# 메모리공간때문에 느린것이라면 배열 사이즈를 작게, 반복횟수를 많이 해서 해결 가능할수도
print(solution([0, 0, 0, 3, 0, 3 ,4]))
print(solution([1, 2, 3, 1]))