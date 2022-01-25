# https://programmers.co.kr/learn/courses/30/lessons/42897
def solution(money):
    # [첫O nX, 첫O nO, 첫X nX, 첫X nO]
    poket = [[0] * 4 for _ in range(len(money))]
    poket[-1][1] = money.pop()
    while money:
        m = money.pop()
        prev = poket.pop()

        poket[-1][0] = max(prev[0], prev[1])
        poket[-1][1] = prev[0] + m

        poket[-1][2] = max(prev[2], prev[3])
        poket[-1][3] = prev[2] + m
    poket[0][1] = 0
    return max(poket[0])


# poket[n] = [[첫집O n집O, 첫집O n집X], [첫집X n집O, 첫집X n집X]]
# 위 방식으로 배열을 크게잡고 반복횟수 줄이기 -> 실패,
# 메모리공간때문에 느린것이라면 배열 사이즈를 작게, 반복횟수를 많이 해서 해결 가능할수도
# 그런거 다 때려치고 pop메소드로 속도 높이고 O(n)으로 구성해서 성공
# 근데 이건 뭐냐 싯ㅅ팔
"""
def solution(a):
    x1, y1, z1 = a[0], a[1], a[0]+a[2]
    x2, y2, z2 = 0, a[1], a[2]
    for i in a[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1)+i
        x2, y2, z2 = y2, z2, max(x2, y2)+i
    return max(x1, y1, y2, z2)
"""
print(solution([0, 0, 0, 3, 0, 3 ,4]))
print(solution([1, 2, 3, 1]))