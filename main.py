from algorithm_lv2.lightCycle import main as test

if __name__ == "__main__":
    testSet = [
        ["SL", "LR"],
        ["S"],
        ["R", "R"]
    ]

    for a in testSet:
        print("answer = ", test.solution(a))
