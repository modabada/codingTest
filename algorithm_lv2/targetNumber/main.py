# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
def solution(numbers, target):
    answer = 0
    cases = [0]
    for num in numbers:
        ar = []
        for case in cases:
            ar.append(case + num)
            ar.append(case - num)
        cases = ar
    for case in cases:
        if case == target:
            answer += 1
    return answer
