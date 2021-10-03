from algorithm_lv2.fixBracket import main as test

if __name__ == "__main__":
    testSet = [
        "(()())()",
        ")(",
        "()))((()"
    ]
    testSet2 = [
        [2, 3, 4],
        [2, 3, 5],
        [2, 3, 4]
    ]
    """
    answer
    2, 1
    1, 3, 2
    """
    for a in testSet:
        print("answer = ", test.solution(a))
