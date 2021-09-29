def solution(scoville, K):
    scoville.sort(reverse=True)
    cnt = 0
    while len(scoville) > 1:
        cnt += 1
        if scoville[-1] + scoville[-2] * 2 > K:
            return cnt
        scoville.pop()
        scoville.pop()
    return -1
