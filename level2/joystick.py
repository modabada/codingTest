# https://programmers.co.kr/learn/courses/30/lessons/42860


def solution(name):
    answer = 0
    check = [True if s != 'A' else False for s in name]
    point = 0
    while True in check:
        if check[point]:
            tmp = ord(name[point]) - 65
            answer += 13 - (tmp - 13) if tmp >= 13 else tmp
            check[point] = False
        cnt = 1
        if True not in check:
            break
        while True:
            if check[point + cnt]:
                answer += cnt
                point += cnt
                break
            elif check[point - cnt]:
                answer += cnt
                point -= cnt
                break
            else:
                cnt += 1
    return answer
