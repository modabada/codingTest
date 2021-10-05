# https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3
def solution(s):
    answer = []
    elements = []
    tmp = set()
    for e in s[2:-2].split('},{'):
        elements.append(set(e.split(',')))
    for e in sorted(elements, key=len):
        answer.append(int((e - tmp).pop()))
        tmp = e
    return answer
