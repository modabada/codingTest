import math
import re


# 자카드 유사도 문제
# 자카드 유사도 = 교집합 / 합집합
# 입력된 문자열을 2개씩 끊어 집합을 만든다  (ex: "testWord" -> "te", "es", "st", "tW", "Wo", "or", "rd")
# 문자 쌍에 알파벳 외의 다른것이 있다면 해당 쌍은 버린다 (ex: "asd2fg" -> "as", "sd", "fg")
# 문자는 대소문자를 구분하지 않는다
# 출력값은 0 ~ 1 의 실수임으로, 보기 쉽게 65536를 곱하고 소수는 버린다
# 교집합과 합집합 모두 공백일 경우 J(a, b) = 1로 정의한다
def solution(str1, str2):
    j1 = list()
    j2 = list()

    reg = re.compile(r'[A-Z]')
    str1 = str1.upper()
    str2 = str2.upper()

    for e in range(1, len(str1)):
        sr = str1[e - 1] + str1[e]
        if sr != ''.join([e.group() for e in re.finditer(reg, sr)]):
            continue
        j1.append(sr)
    for e in range(1, len(str2)):
        sr = str2[e - 1] + str2[e]
        if sr != ''.join([e.group() for e in re.finditer(reg, sr)]):
            continue
        j2.append(sr)

    temp = j1.copy()
    set_sum = j1.copy()

    for e in j2:
        if e not in temp:
            set_sum.append(e)
        else:
            temp.remove(e)

    inter = list()
    for e in j2:
        if e in j1:
            j1.remove(e)
            inter.append(e)

    if len(set_sum) == 0:
        answer = 1
    else:
        answer = len(inter) / len(set_sum)
    return math.floor(answer * 65536)
