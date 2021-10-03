from algorithm_lv2.menuRenewal import main as test

if __name__ == "__main__":
    testSet = [
        ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
        ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
        ["XYZ", "XWY", "WXA"]
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
    for a, b in zip(testSet, testSet2):
        print("answer = ", test.solution(a, b))
