# https://school.programmers.co.kr/learn/courses/30/lessons/178871


def solution(players, callings):
    d = dict()
    for i in range(len(players)):
        d[players[i]] =  i
    for c in callings:
        rank = d[c]
        d[c] -= 1
        d[players[rank - 1]] += 1
        players[rank], players[rank - 1] = players[rank - 1], players[rank]
        # print(players)
    return players
