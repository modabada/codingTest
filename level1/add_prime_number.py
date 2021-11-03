# https://programmers.co.kr/learn/courses/30/lessons/12977


def solution(nums: list):
    answer = 0
    for x in range(0, len(nums)):
        for y in range(x + 1, len(nums)):
            for z in range(y + 1, len(nums)):
                answer += 1
                n = nums[x] + nums[y] + nums[z]
                for i in range(2, (int(n ** 0.5) + 1)):
                    if n % i == 0:
                        answer -= 1
                        break
    return answer
