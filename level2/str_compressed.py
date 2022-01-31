# https://programmers.co.kr/learn/courses/30/lessons/60057


def solution(x: list):
    answer = len(x)
    for i in range(1, len(x) + 1):
        n = 0
        patton = str()
        compressed = list()
        for j in range(len(x)):
            if n >= len(x):
                break
            if patton == x[n:n + i]:
                compressed[-2] += 1
            else:
                patton = x[n:n + i]
                compressed.append(1)
                compressed.append(''.join(patton))
            n += i
        for j in range(compressed.count(1)):
            compressed.remove(1)
        compressed = ''.join(map(str, compressed))
        if answer > len(compressed):
            answer = len(compressed)
    return answer
