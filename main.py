from heap.disc_control import main as test

if __name__ == "__main__":
    testSet = [
        [[0, 3], [1, 9], [2, 6]]
    ]

    for a in testSet:
        print("answer = ", test.solution(a))
