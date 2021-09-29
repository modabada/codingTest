from algorithm_lv2.countOf124 import main as test

if __name__ == "__main__":
    testSet = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]
    """
    answer
    1, 2, 4 11
    """
    for e in testSet:
        print("answer = ", test.solution(e))
