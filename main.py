from algorithm_lv2.functionDevelopment import main as test

if __name__ == "__main__":
    testSet = [
        [93, 30, 55],
        [95, 90, 99, 99, 80, 99]
    ]
    testSet2 = [
        [1, 30, 5],
        [1, 1, 1, 1, 1, 1]
    ]
    """
    answer
    2, 1
    1, 3, 2
    """
    for e, i in zip(testSet, testSet2):
        print("answer = ", test.solution(e, i))
