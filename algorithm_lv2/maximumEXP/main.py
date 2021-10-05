# https://programmers.co.kr/learn/courses/30/lessons/67257
from itertools import permutations


def calculate(expression, ops):
    nums = list()
    operator = list()
    tmp = ''
    for e in expression:
        if e not in [str(n) for n in range(0, 10)]:
            nums.append(int(tmp))
            operator.append(e)
            tmp = ''
        else:
            tmp += e
    nums.append(int(tmp))

    for op in ops:
        i = 0
        while i < len(operator):
            if operator[i] == op:
                if op == '*':
                    nums[i] *= nums[i + 1]
                elif op == '+':
                    nums[i] += nums[i + 1]
                else:
                    nums[i] -= nums[i + 1]
                del nums[i + 1]
                del operator[i]
                i -= 1
            i += 1
    return abs(nums[0])


solution = lambda expression: max([calculate(expression, ops) for ops in permutations(['*', '+', '-'], 3)])
