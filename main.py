from algorithm_lv2.targetNumber import main as test

if __name__ == "__main__":
    testSet = [
        [1, 1, 1, 1, 1]
    ]
    testSet2 = [
        3
    ]
    """
    answer
    2, 1
    1, 3, 2
    """
    for e, i in zip(testSet, testSet2):
        print("answer = ", test.solution(e, i))
