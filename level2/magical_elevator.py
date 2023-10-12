# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    answer = 0
    
    while storey > 0:
        e = storey % 10
        storey = storey // 10
        if e < 5:
            answer += e
        elif e > 5:
            answer += 10 - e
            storey += 1
        else:   
            if storey % 10 >= 5:
                answer += 5
                storey += 1
            else:
                answer += 5
    return answer
