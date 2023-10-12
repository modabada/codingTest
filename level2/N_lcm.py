# https://school.programmers.co.kr/learn/courses/30/lessons/12953

import math


def solution(arr):
    for i in range(len(arr) - 1):
        gcd = math.gcd(arr[i], arr[i + 1])
        lcm = arr[i] * arr[i + 1] // gcd
        arr[i + 1] = lcm
    return arr[-1]
