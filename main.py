from kit.greedy import connect_island as test

if __name__ == "__main__":
    set1 = [
        4
    ]
    set2 = [
        [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    ]

    for x, y in zip(set1, set2):
        print("answer = ", test.solution(x, y))
