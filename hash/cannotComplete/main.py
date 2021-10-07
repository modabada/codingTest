# https://programmers.co.kr/learn/courses/30/lessons/42576
solution = lambda participant, completion: \
    [x for x, y in zip(sorted(participant), sorted(completion + ['z'])) if x != y][0]
