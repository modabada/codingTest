# https://programmers.co.kr/learn/courses/30/lessons/81301
# 입력으로 숫자와 영문이 섞여 입력되고
# 출력으로 해당 입력을 모두 숫자로 변환


def solution(s):
    answer = 0
    temp = []
    i = 0
    en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for e in s:
        inx = 0
        if e in n:
            inx = int(e)
        else:
            temp.append(e)
            if ''.join(temp) in en:
                inx = en.index(''.join(temp))
                temp = []
            else:
                continue
        answer = answer * 10 + inx
        i += 1
    return answer
