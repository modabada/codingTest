# https://programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    return sum([e if signs[i] else e * -1 for i, e in enumerate(absolutes)])
