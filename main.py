from algorithm_lv2.moreSpicy import main as test

if __name__ == "__main__":
    testSet = [
        [1, 2, 3, 9, 10, 12],
        [1, 2, 3, 4, 5, 6],
        [0, 0, 0, 0, 0]
    ]
    testSet2 = [
        7,
        1000,
        1
    ]
    """
    answer
    2, 1
    1, 3, 2
    """
    for e, i in zip(testSet, testSet2):
        print("answer = ", test.solution(e, i))
