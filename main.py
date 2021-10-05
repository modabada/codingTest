from algorithm_lv2.tuple import main as test

if __name__ == "__main__":
    testSet = [
        "{{2},{2,1},{2,1,3},{2,1,3,4}}",
        "{{1,2,3},{2,1},{1,2,4,3},{2}}",
        "{{20,111},{111}}",
        "{{123}}",
        "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    ]

    for a in testSet:
        print("answer = ", test.solution(a))
