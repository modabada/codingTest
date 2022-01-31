# https://programmers.co.kr/learn/courses/30/lessons/43238#qna

def solution(n, times):
    answer = 0
    min_time = 1
    max_time = 1000000000 * n
    while min_time <= max_time:
        mid = (min_time + max_time) // 2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        if people >= n:
            answer = mid
            max_time = mid - 1
        else:
            min_time = mid + 1
    return answer

# �ּ�, �ִ� ���, mid�� ���ؼ� �� mid������ ����� n���� ��� ó���� �� �ֳ�?
# -> �ִٸ� �� ���� �ð����ε� ó�� �����̶� �Ҹ��� �ִ븦 mid - 1�� �缳�� �� �ݺ�
# -> ���ٸ� ���� �ð����� ó�� �Ұ����ϴٴ� �Ҹ��� �ּҸ� mid + 1�� �缳�� �� �ݺ�
# ���� ������ �ּ�, �ִ�ð��� ��ĥ ������ �ݺ� �� ������ ��ȯ
