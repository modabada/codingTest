from algorithm_lv1.makePrimeNumber import main as test

if __name__ == "__main__":
    testSet = [
        [1, 2, 3, 4],
        [1, 2, 7, 6, 4]
    ]
    # answer == 1, 4
    for e in testSet:
        print("answer = ", test.solution(e))
