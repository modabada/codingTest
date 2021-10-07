from algorithm_lv2.phoneBook import main as test

if __name__ == "__main__":
    testSet = [
        ["119", "97674223", "1195524421"]
    ]

    for a in testSet:
        print("answer = ", test.solution(a))
