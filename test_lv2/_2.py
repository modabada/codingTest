import math
import re


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
