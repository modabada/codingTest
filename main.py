from algorithm_lv2.phoneBook import main as test

if __name__ == "__main__":
    testSet = [
        ["119", "97674223", "1195524421"],
        ["123", "456", "789"],
        ["12", "123", "1235", "567", "88"]
    ]

    for a in testSet:
        print("answer = ", test.solution(a))
