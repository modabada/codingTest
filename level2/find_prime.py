# https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations


def solution(numbers):
    answer = 0
    comb = [e for e in [list(set(permutations(numbers, r))) for r in range(1, len(numbers) + 1)]]
    for e in comb:
        for n in e:
            if n[0] == '0'or n == ('1',):
                continue
            n = int(''.join(n))
            answer += 1
            for i in range(2, (int(n ** 0.5) + 1)):
                    if n % i == 0:
                        answer -= 1
                        break
    return answer
