# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville, K):
    H = []
    for e in scoville:
        heapq.heappush(H, e)
    cnt = 0
    while H[0] < K and len(H) > 1:
        cnt += 1
        mixed = heapq.heappop(H) + heapq.heappop(H) * 2
        heapq.heappush(H, mixed)
    return -1 if H[0] < K else cnt
