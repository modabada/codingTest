# https://programmers.co.kr/learn/courses/30/lessons/42888


def solution(record):
    answer = []
    name = dict()
    for e in record:
        e = e.split(' ')
        if e[0] == 'Leave':
            answer.append([e[1], '님이 나갔습니다.'])
        else:
            name[e[1]] = e[2]
            if e[0] == 'Enter':
                answer.append([e[1], '님이 들어왔습니다.'])
    for i in range(len(answer)):
        answer[i] = name[answer[i][0]] + answer[i][1]
    return answer
