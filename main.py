from algorithm_lv2.removeThatPair import main as test

if __name__ == "__main__":
    testSet = [
        "baabaa",
        "cdcd"
    ]
    testSet2 = [
        1, 0
    ]
    """
    answer
    2, 1
    1, 3, 2
    """
    for e, i in zip(testSet, testSet2):
        print("answer = ", test.solution(e))
