# https://programmers.co.kr/learn/courses/30/lessons/42579


def solution(genres, plays):
    answer = list()
    song = dict()
    for i, e in enumerate(zip(genres, plays)):
        if e[0] not in song:
            song[e[0]] = [e[1], i]
        else:
            song[e[0]][0] += e[1]
            song[e[0]].append(i)

    for s in sorted(song.values(), reverse=True):
        s = sorted(s[1:], key=lambda f: (plays[f], -f))
        # s = sorted([(plays[e], e) for e in s[1:]])
        answer.append(s.pop())
        if s:
            answer.append(s.pop())
    return answer
