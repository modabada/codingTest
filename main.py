from algorithm_lv1.cannotComplete import main as test

if __name__ == "__main__":
    testSet = [
        [1, 2, 3, 4],
        [1, 2, 7, 6, 4]
    ]

    part = [
        ["leo", "kiki", "eden"],
        ["marina", "josipa", "nikola", "vinko", "filipa"],
        ["mislav", "stanko", "mislav", "ana"]
    ]
    com = [
        ["eden", "kiki"],
        ["josipa", "filipa", "marina", "nikola"],
        ["stanko", "ana", "mislav"]
    ]
    # answer == 1, 4
    for x, y in zip(part, com):
        print('answer = ', test.solution(x, y))
    """for e in testSet:
        print("answer = ", test.solution(e))"""
