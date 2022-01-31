# https://programmers.co.kr/learn/courses/30/lessons/42746


def solution(numbers):
    if numbers == [0 for _ in range(0, len(numbers))]:
        return '0'
    ls = [[(e * 4)[:4], e] for e in map(str, numbers)]
    ls.sort(reverse=True)
    ls = ''.join([e[1] for e in ls])
    return ''.join(ls)
