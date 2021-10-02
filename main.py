from algorithm_lv2.keepDistance import main as test

if __name__ == "__main__":
    testSet = [
        [
            [
                "POOOP",
                "OXXOX",
                "OPXPX",
                "OOXOX",
                "POXXP"
            ],
            [
                "POOPX",
                "OXPXP",
                "PXXXO",
                "OXXXO",
                "OOOPP"
            ],
            [
                "PXOPX",
                "OXOXP",
                "OXPOX",
                "OXXOP",
                "PXPOX"
            ],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
        ]
    ]

    for a in testSet:
        print("answer = ", test.solution(a))
