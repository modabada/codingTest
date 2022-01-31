# https://programmers.co.kr/learn/courses/30/lessons/42895
def solution(N, number):
    arr = []
    for i in range(8):
        numbers = set()
        numbers.add(int(str(N) * (i + 1)))
        for j in range(i):
            for x in arr[j]:
                for y in arr[-j - 1]:
                    numbers.add(x + y)
                    numbers.add(x * y)
                    numbers.add(x - y)
                    if y != 0:
                        numbers.add(x // y)
        if number in numbers:
            return i + 1
        arr.append(numbers)
    return -1
