from algorithm_lv2.maximumEXP import main as test

if __name__ == "__main__":
    testSet = [
        "100-200*300-500+20",
        "50*6-3*2"
    ]

    for a in testSet:
        print("answer = ", test.solution(a))
