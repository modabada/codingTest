# https://programmers.co.kr/learn/courses/30/lessons/43236#qna

def solution(distance, rocks, n):
    rocks.sort()
    min_dis = 1
    max_dis = distance
    answer = 0

    while min_dis <= max_dis:
        mid = (min_dis + max_dis) // 2
        cnt = 0
        last = 0
        for rock in rocks:
            gab = rock - last
            if gab < mid:
                cnt += 1
            else:
                last = rock
        # 마지막 바위와 distance에 놓인 바위에 대해 검사(마지막 바위니 last 갱신 필요없음)
        if distance - rocks[-1] < mid:
            cnt += 1

        if cnt > n:
            max_dis = mid - 1
        else:
            min_dis = mid + 1
            answer = mid
    return answer

# 이분탐색 결과 -> 최소거리
# 바위의 거리가 mid 보다 작으면 cnt 증가 및 last 비갱신(바위를 파괴했음)
# cnt > mid면 이분값의 아래에 대해 반복
# cnt < mid면 이분값의 상위에 대해 반복, answer는 임시로 mid로 설정
p1 = [
    25
]
p2 = [
    [2, 14, 11, 21, 17]
]
p3 = [2
]
ans = [
    3
]

for a, b, c, d in zip(p1, p2, p3, ans):
    sol = solution(a, b, c)
    print(True if sol == d else sol)