def solution(N, number):
    # dfs is never can`t, solution(1, 122)  
    # but wfs can find min answer
    arr = [int(str(N) * i) for i in range(1, 9)]
    return -1




t1 = [
    5, 12
]
t2 = [
    12, 11
]
ans = [
    4, 3
]
[print(solution(t1[i], t2[i])) for i in range(len(t1))]


