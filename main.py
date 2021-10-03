from algorithm_lv2.newsClustering import main as test

if __name__ == "__main__":
    testSet = [
        "FRANCE",
        "handshake",
        "aa1+aa2",
        "E=M*C^2"
    ]
    testSet2 = [
        "french",
        "shake hands",
        "AAAA12",
        "e=m*c^2"
    ]
    """
    answer
    2, 1
    1, 3, 2
    """
    for a, b in zip(testSet, testSet2):
        print("answer = ", test.solution(a, b))
