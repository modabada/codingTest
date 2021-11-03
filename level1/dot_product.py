# https://programmers.co.kr/learn/courses/30/lessons/70128


def solution(a, b):
    dsum=0
    for n in range(0,len(a)):
        sum1=a[n]*b[n]
        dsum = dsum+sum1
    return dsum
