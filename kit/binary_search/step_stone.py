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
        # ������ ������ distance�� ���� ������ ���� �˻�(������ ������ last ���� �ʿ����)
        if distance - rocks[-1] < mid:
            cnt += 1

        if cnt > n:
            max_dis = mid - 1
        else:
            min_dis = mid + 1
            answer = mid
    return answer

# �̺�Ž�� ��� -> �ּҰŸ�
# ������ �Ÿ��� mid ���� ������ cnt ���� �� last �񰻽�(������ �ı�����)
# cnt > mid�� �̺а��� �Ʒ��� ���� �ݺ�
# cnt < mid�� �̺а��� ������ ���� �ݺ�, answer�� �ӽ÷� mid�� ����
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