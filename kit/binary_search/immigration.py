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

# 최소, 최대 잡고, mid값 구해서 이 mid값으로 대기자 n명을 모두 처리할 수 있냐?
# -> 있다면 더 적은 시간으로도 처리 가능이란 소리니 최대를 mid - 1로 재설정 후 반복
# -> 없다면 지금 시간으로 처리 불가능하다는 소리니 최소를 mid + 1로 재설정 후 반복
# 위의 동작을 최소, 최대시간이 겹칠 때까지 반복 후 최종값 반환
