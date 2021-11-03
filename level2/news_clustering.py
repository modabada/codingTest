# https://programmers.co.kr/learn/courses/30/lessons/17677
import re


def solution(str1, str2):
    j1 = list()
    j2 = list()

    str1 = str1.upper()
    str2 = str2.upper()
    reg = re.compile(r'[A-Z]{2}')
    for i in range(1, len(str1)):
        temp = str1[i - 1: i + 1]
        if reg.match(temp):
            j1.append(temp)
    for i in range(1, len(str2)):
        temp = str2[i - 1: i + 1]
        if reg.match(temp):
            j2.append(temp)

    inter = list()
    tmp = j1[:]
    for e in j2:
        if e in tmp:
            tmp.remove(e)
            inter.append(e)

    union = j1 + j2
    for e in inter:
        union.remove(e)
        
    answer = 1 if not union else len(inter) / len(union)
    return int(answer * 65536)
