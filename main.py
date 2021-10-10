from hash.camouflage import main as test

if __name__ == "__main__":
    testSet = [
        [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]],
        [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    ]

    for a in testSet:
        print("answer = ", test.solution(a))
