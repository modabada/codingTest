from algorithm_lv2 import strCompression as test

if __name__ == "__main__":
    testSet = [
        "aabbaccc",
        "ababcdcdababcdcd",
        "abcabcdede",
        "abcabcabcabcdededededede",
        "xababcdcdababcdcd"
    ]
    # answer == 7 9 8 14 17
    for e in testSet:
        print("answer = ", test.solution(e))
