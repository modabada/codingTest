# https://programmers.co.kr/learn/courses/30/lessons/42840


def solution(answers):
    s1 = range(1, 6)
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    grade = [[0, i] for i in range(1, 4)]
    for i, ans in enumerate(answers):
        if s1[i % 5] == ans:
            grade[0][0] += 1
        if s2[i % 8] == ans:
            grade[1][0] += 1
        if s3[i % 10] == ans:
            grade[2][0] += 1

    grade.sort(key=lambda x: x[0], reverse=True)
    maxV = grade[0][0]
    answer = [e[1] for e in grade if e[0] == maxV]
    return sorted(answer)
