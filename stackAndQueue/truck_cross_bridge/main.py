# https://programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque as queue


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = queue([0] * bridge_length)
    truck_weights = truck_weights[::-1]
    now_weight = 0
    while truck_weights:
        answer += 1
        truck = truck_weights.pop()
        now_weight -= bridge.popleft()
        while now_weight + truck > weight:
            answer += 1
            now_weight -= bridge.popleft()
            bridge.append(0)
        bridge.append(truck)
        now_weight += truck
    answer += bridge_length
    return answer
