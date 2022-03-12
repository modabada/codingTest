# https://programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    minV = 0
    maxV = max(stones)
    answer = 0
    while minV <= maxV:
        mid = (minV + maxV) // 2
        times0 = 0
        for s in stones:
            if s > mid:
                times0 = 0
            else:
                times0 += 1
            
            if times0 > k:
                break
        if times0 < k:
            minV = mid + 1
        else:
            maxV = mid - 1
            answer = mid
    return answer
